# my-package

A modern Python project template with tests, linting, type checking, and
GitHub Actions CI. Conda manages the Python version; Poetry manages the
packages.

<!-- template-setup:start -->
## Using this template

1. On GitHub, click **Use this template** (enable it under
   *Settings → General → Template repository*), then clone your new repo.
2. Pick a name for your project. It is used for the conda environment, the
   Python package, and the Poetry project. Letters, digits, `_` and `-` are
   allowed; `my-project` gives the package `my_project` and the command
   `my-project`.

   Linux / macOS:
   ```bash
   export ENV_NAME=my_project
   ```

   Windows (Command Prompt):
   ```bat
   set ENV_NAME=my_project
   ```
3. Run the rename script from the repository root. It renames the `my_package/`
   folder, updates `pyproject.toml`, `environment.yml`, `tests/`, `.github/`
   and this README, removes this section, and then deletes itself.

   Linux / macOS:
   ```bash
   python3 scripts/rename_package.py
   ```

   Windows (Command Prompt):
   ```bat
   python scripts\rename_package.py
   ```
4. Update the author and license details in `pyproject.toml` and `LICENSE`.
5. Commit the rename, then continue with the setup below.
<!-- template-setup:end -->

## Set your environment name first

Type your environment (and Python package) name once. Every command below uses
it, so you can copy and paste them as-is. Run this again in any new terminal.

Linux / macOS:
```bash
export ENV_NAME=my_package
```

Windows (Command Prompt):
```bat
set ENV_NAME=my_package
```

## Development setup

Install Miniconda first: https://docs.anaconda.com/miniconda/

Create the environment from `environment.yml` (Python, IPython, and Poetry),
then activate it.

Linux / macOS:
```bash
conda env create -f environment.yml
conda activate "$ENV_NAME"
```

Windows (Command Prompt):
```bat
conda env create -f environment.yml
conda activate %ENV_NAME%
```

Then, from the folder containing `pyproject.toml`, install the packages and the
git hooks:

```bash
poetry install
pre-commit install
```

Poetry installs into the active conda environment. You can confirm with
`poetry env info`.

| Task          | Command                       |
| ------------- | ----------------------------- |
| Run tests     | `pytest`                      |
| Lint          | `ruff check .`                |
| Format        | `ruff format .`               |
| Type check    | `mypy`                        |
| Add a package | `poetry add <package>`        |
| Add a dev tool | `poetry add --group dev <package>` |

## Updating the environment file

If you change the Python version or add a conda package, edit
`environment.yml` and update the environment:

```bash
conda env update -f environment.yml --prune
```

## Removing the environment

Linux / macOS:
```bash
conda remove --name "$ENV_NAME" --all
```

Windows (Command Prompt):
```bat
conda remove --name %ENV_NAME% --all
```

## What's included

- Conda environment (`environment.yml`) with Poetry for dependency management
- pytest + coverage
- Ruff (lint + format) and strict mypy
- pre-commit hooks
- GitHub Actions CI using conda + Poetry (lint + tests on Python 3.10–3.13)
- Dependabot, PR template, and issue templates

## Resources

- [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Poetry basic usage](https://python-poetry.org/docs/basic-usage/)

## License

MIT
