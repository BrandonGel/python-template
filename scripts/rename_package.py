"""Rename the template's ``my_package`` to the name set in ``ENV_NAME``.

Usage (from the repository root)::

    export ENV_NAME=my_project        # Windows (cmd): set ENV_NAME=my_project
    python3 scripts/rename_package.py

``ENV_NAME`` is used for the conda environment, the README, the Python package,
and the Poetry project. The conda environment (``environment.yml``) and the
README use the name exactly as typed. Python needs underscores, so the package
folder and import name replace hyphens with underscores, while the
command-line tool uses hyphens: ``my-project`` gives the environment and README
name ``my-project``, the package ``my_project``, and the command ``my-project``.

The script renames the package folder, updates every reference to
``my_package`` / ``my-package`` (and the ``my_project`` / ``my-project``
examples in the README), removes the "Using this template" section from the
README, and then deletes itself. It uses only the standard library.
"""

from __future__ import annotations

import keyword
import os
import re
import sys
from pathlib import Path

OLD_PACKAGE = "my_package"
OLD_CLI = "my-package"
# Placeholder names shown in the README's examples.
EXAMPLE_NAMES = ("my_project", "my-project")
# Files that name the project rather than the Python package: they use ENV_NAME
# exactly as typed, so `conda activate "$ENV_NAME"` works as written.
ENV_NAME_FILES = {"README.md", "environment.yml"}

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    ".pytest_cache",
    "scripts",
}
# .templatesyncignore must keep naming the template's own my_package/ folder, so
# template-sync does not re-add the sample code after the package is renamed.
SKIP_FILES = {"poetry.lock", ".templatesyncignore"}
NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
SETUP_SECTION = re.compile(
    r"<!-- template-setup:start -->.*?<!-- template-setup:end -->\n*",
    re.DOTALL,
)


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_name() -> tuple[str, str, str]:
    """Return ``(env, package, cli)`` names derived from ``ENV_NAME``."""
    name = os.environ.get("ENV_NAME", "").strip()
    if not name:
        fail(
            "ENV_NAME is not set.\n"
            "  Linux / macOS:   export ENV_NAME=my_project\n"
            "  Windows (cmd):   set ENV_NAME=my_project"
        )
    if not NAME_PATTERN.match(name):
        fail(
            f"ENV_NAME={name!r} is not valid. Start with a letter and use only "
            "letters, digits, '_' and '-'."
        )
    package = name.replace("-", "_")
    if keyword.iskeyword(package):
        fail(f"{package!r} is a Python keyword; choose another name.")
    return name, package, name.replace("_", "-")


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if not path.is_file() or path.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        files.append(path)
    return files


def main() -> int:
    env, package, cli = read_name()

    old_dir = ROOT / OLD_PACKAGE
    new_dir = ROOT / package
    if not old_dir.is_dir():
        fail(f"{OLD_PACKAGE}/ not found. Has this template already been renamed?")
    if package == OLD_PACKAGE:
        print(f"ENV_NAME is already '{OLD_PACKAGE}'; nothing to rename.")
        return 0
    if new_dir.exists():
        fail(f"{package}/ already exists.")

    old_dir.rename(new_dir)

    changed: list[str] = []
    for path in text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # binary file
        updated = text
        if path.name == "README.md":
            updated = SETUP_SECTION.sub("", updated)
        if path.name in ENV_NAME_FILES:
            for old in (OLD_PACKAGE, OLD_CLI, *EXAMPLE_NAMES):
                updated = updated.replace(old, env)
        else:
            updated = updated.replace(OLD_PACKAGE, package).replace(OLD_CLI, cli)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="")
            changed.append(str(path.relative_to(ROOT)))

    print(f"Renamed {OLD_PACKAGE}/ -> {package}/")
    for name in changed:
        print(f"Updated {name}")

    try:
        Path(__file__).resolve().unlink()
        scripts_dir = ROOT / "scripts"
        if not any(scripts_dir.iterdir()):
            scripts_dir.rmdir()
        print("Removed scripts/rename_package.py")
    except OSError:
        print("Could not remove scripts/rename_package.py; delete it yourself.")

    print(
        "\nNext steps:\n"
        "  conda env create -f environment.yml\n"
        f"  conda activate {env}\n"
        "  poetry install\n"
        "  pre-commit install"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
