# 🐍 Python Project Template with pyenv, pip-tools, and black

Welcome! This is a minimal Python project template to help you write clean, manageable Python code — with modern tooling for formatting and dependency management.

---

## 📦 Prerequisites

### ✅ Use `pyenv` to manage your Python version

It’s recommended to use [pyenv](https://github.com/pyenv/pyenv) to install and manage Python versions. This project is currently using version 3.13.0

### Install `pip-tools` to manage requirements

```
pip install pip-tools
```

### Adding a new package

##### 1. Add the package name to `requirements.in` (for production/runtime dependencies) OR to `dev-requirements.in` (for development-only dependencies).

##### 2. Recompile requirements files:

`requirements.txt`:

```
pip-compile
```

`dev-requirements.txt`:

```
pip-compile dev-requirements.in
```

##### 3. Install the updated packages and remove any obsolete ones:

`requirements.txt`:

```
pip-sync
```

`dev-requirements.txt`:

```
pip-sync dev-requirements.txt
```

Useful links:

- https://suyojtamrakar.medium.com/managing-your-requirements-txt-with-pip-tools-in-python-8d07d9dfa464
- https://www.getorchestra.io/guides/ruff-vs-black-formatter-linting-and-formatting-in-vscode
