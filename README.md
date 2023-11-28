# OpenXcom Generator

## Installation
Be sure to execute this from a non-venv shell

```shell
git clone git@github.com:bluemapping/compute.git
cd compute
virtualenv venv
source .venv/bin/activate
pip install poetry
poetry install
pre-commit install
pre-commit install --hook-type commit-msg
```

## Commands

### Tools
- Check lint

```shell
poetry run ruff src 
```

- Fix code formatting
```shell
poetry run black src 
```

- Run tests
```shell
poetry run pytest 
```

- Static typing
```shell
poetry run mypy src 
```

### Build
- Build docker image locally
```shell
docker build -t compute .
```
- Run docker image locally
```shell
docker run --rm compute
```

## Package management
Poetry: https://python-poetry.org/

## Quality

### Tools
#### Linter
Ruff: https://docs.astral.sh/ruff/

#### Prettier
Black: https://black.readthedocs.io/en/stable/

#### Tests
PyTest: https://docs.pytest.org/en/7.4.x/

#### Conventional Pre-Commits
Using the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/#summary) through the [conventional-pre-commit package](https://github.com/compilerla/conventional-pre-commit)

#### Hooks
PreCommit: https://pre-commit.com/

#### Static typing
Using mypy


### CI
[Github Actions](https://docs.github.com/en/actions) is the integrated Continuous Integration and Deployment tool in GitHub

The deployment history is available [under the Actions tab](https://github.com/bluemapping/compute/actions/)

Notable workflows use cases are:
- `validate` on push on an allowed branch.


## Recommended IDE PyCharm Configuration
### Plugins
Ruff: Settings > Plugins > Marketplace > "Ruff"

### Actions on save
Black: Settings > Tools > Black
- On Code Reformat
- On save
  both need to be checked.

### File nesting
Project tool window | '...' (vertical) | "File Nesting..."
Set (click on the '+' sign)
- 'Parent File Suffix': '.py'
- 'Child File Suffix': '_spec.py'

