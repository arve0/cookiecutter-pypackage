# {{ cookiecutter.repo_name }}

[![build-status-image]][travis]
[![pypi-version]][pypi]
[![wheel]][pypi]

## Overview

{{ cookiecutter.project_short_description }}

## Installation

Install using `pip`...

```bash
pip install {{ cookiecutter.repo_name }}
```

## Example

TODO: Write example.

## API reference

API reference is at http://{{ cookiecutter.repo_name }}.rtfd.org.

## Development
Install dependencies and link development version of {{ cookiecutter.repo_name }} to pip:
```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
cd {{ cookiecutter.repo_name }}
pip install -r requirements.txt # install dependencies and {{ cookiecutter.repo_name }}-package
```

### Testing
```bash
tox
```

### Build documentation locally
To build the documentation:
```bash
pip install -r docs/requirements.txt
make docs
```



[build-status-image]: https://secure.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
[travis]: http://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
[pypi-version]: https://pypip.in/version/{{ cookiecutter.repo_name }}/badge.svg
[pypi]: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
[wheel]: https://pypip.in/wheel/{{ cookiecutter.repo_name }}/badge.svg
