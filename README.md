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

## Keeping up with the template

Repos created from this template get a weekly **Template sync** workflow
(`.github/workflows/template-sync.yml`, using
[actions-template-sync](https://github.com/AndreasAugustin/actions-template-sync)).
When the template changes, it opens a pull request labelled `template_sync` in
your repo, and nothing changes until you merge it.

One-time setup in each new repo: go to *Settings → Actions → General →
Workflow permissions* and tick **Allow GitHub Actions to create and approve
pull requests**. To check for updates right away, open the *Actions* tab, pick
**Template sync**, and click **Run workflow**.

What gets synced is controlled by `.templatesyncignore` (one git pathspec per
line). Out of the box your own code, tests, `pyproject.toml`, `poetry.lock`,
`environment.yml`, `README.md` and `LICENSE` are never touched, so the PRs only
carry shared tooling such as `.gitignore`, `.pre-commit-config.yaml`,
Dependabot settings and the issue and PR templates. Add any shared file you have
customised to `.templatesyncignore`, or the next sync PR will overwrite it.

CI updates are skipped by default, because the built-in `GITHUB_TOKEN` is not
allowed to change files under `.github/workflows/`. To sync those too, create a
personal access token with the `workflow` scope, save it as the repo secret
`TEMPLATE_SYNC_TOKEN`, and remove the `.github/workflows/` line from
`.templatesyncignore`.

The workflow pulls from `BrandonGel/python-template`. If you copied this
template under another name, change `source_repo_path` in the workflow file.

## What's included

- Conda environment (`environment.yml`) with Poetry for dependency management
- pytest + coverage
- Ruff (lint + format) and strict mypy
- pre-commit hooks
- GitHub Actions CI using conda + Poetry (lint + tests on Python 3.10–3.13)
- Dependabot, PR template, and issue templates
- Weekly template-sync workflow that opens a PR when the template changes

## Resources

- [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Poetry basic usage](https://python-poetry.org/docs/basic-usage/)

## License

MIT
