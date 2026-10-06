# my-package

A modern Python project template with tests, linting, type checking, and
GitHub Actions CI.

## Using this template

1. On GitHub, click **Use this template** (enable it under
   *Settings → General → Template repository*).
2. Rename the package:
   - Rename `my_package/` to your package name.
   - Find and replace `my_package` / `my-package` in `pyproject.toml`,
     `tests/`, `README.md`, and `.github/`.
   - Update the author and license details.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

| Task          | Command                       |
| ------------- | ----------------------------- |
| Run tests     | `pytest`                      |
| Lint          | `ruff check .`                |
| Format        | `ruff format .`               |
| Type check    | `mypy`                        |

## What's included

- Flat package layout packaged with Hatchling
- pytest + coverage
- Ruff (lint + format) and strict mypy
- pre-commit hooks
- GitHub Actions CI (lint + tests on Python 3.10–3.13)
- Dependabot, PR template, and issue templates

## License

MIT
