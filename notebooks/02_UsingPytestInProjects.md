# Exercise — convert notebook to a proper package + tests

## Goal: 

**take the code and tests from the notebook `01_UnitTestingWithPytest.ipynb` and turn them into a small git repository with a standard src/ tests/ layout and runnable tests with PyTest.**


## Steps 

### 1. Create a new repo (git init) and project layout:

```
<project_name>
|
├── src/
|   ├── mathlib/
|   |   ├── __init__.py
|   |   └── <module>.py
├── tests/
|   ├── conftest.py
|   └── test_<group>.py
|
├── pyproject.toml
├── .gitignore
└── README.md
```
    
Reference: [Reference_Standard_Project_Organization.ipynb](Reference_Standard_Project_Organization.ipynb)

`UV` also does a fantastic job getting things set up correctly from the beginning: https://docs.astral.sh/uv/getting-started/features/#python-versions



### 2. Connect the Folders using the `pyproject.toml` packaging format:


https://packaging.python.org/en/latest/tutorials/packaging-projects/

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "hhai-workshop"
version = "0.0.0"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
test = ["pytest"]

[tool.hatch.build.targets.wheel]
packages = ["src/hhai_workshop"]
```

- Install the `src` packages in "development" (a.k.a. "editable") mode:
    - Using pip: `python -m pip install -e ".[test]"`
    - Using uv: `uv pip install -e ".[test]"` or `uv sync --extra test`



### 3. Extract code/tests from the notebook:

For each test/src pair:
    
  1. open the notebook, copy library-code cells into modules under src/<your_pkg>/ (e.g. src/<your_pkg>/<module>.py).
  2. copy test cells into tests/test_*.py files, adapt imports to use your package (from <your_pkg> import ...).
  3. Run the tests (`uv run pytest`), confirm they are detected and pass.

