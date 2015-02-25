# {{ cookiecutter.repo_name }}

[![build-status-image]][travis]
[![pypi-version]][pypi]

## Overview

{{ cookiecutter.project_short_description }}

## Requirements

* Python (2.7, 3.4)

## Installation

Install using `pip`...

```bash
pip install {{ cookiecutter.repo_name }}
```

## Example

TODO: Write example.

## Testing

Install testing requirements:

```bash
pip install tox
```

Run:

```bash
tox
```

## Documentation

To build the documentation, you'll need sphinx:

```bash
pip install -r docs/requirements.txt
```

To build the documentation:

```bash
cd docs
make html && open _build/html/index.html
```


[build-status-image]: https://secure.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
[travis]: http://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
[pypi-version]: https://pypip.in/version/{{ cookiecutter.repo_name }}/badge.svg
[pypi]: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
