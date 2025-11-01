# Python App Template

This is a template for easily bootstrap a Python project using:

- Python 3.12.8
- FastAPI standard
- Pytest
- UV for dependencies management

## Creating this Template

1. Creating a project using UV:

```sh
uv init python_app_template
```

2. Creating (and downloading if it not found) a specific Python version:

```sh
uv venv --python 3.12
```

3. Activating a Python virtual environment:

```sh
source .venv/bin/activate
```

4. Adding FastAPI to the project:

```sh
uv add fastapi
```

5. Adding Pytest to the project for development environment:

```sh
uv add pytest --dev
```

6. Installing cookiecutter with uv:

```sh
uv pip install cookiecutter
```

## Using this Template

To create a new project using this template, run the following command:

```sh
cookiecutter fastapi_uv_template
```

Replace `fastapi_uv_template` with the local path or URL to this template repository.