#!/usr/bin/env python

import os
import sys
from setuptools import setup

os.system('make rst')
try:
    readme = open('README.rst').read()
except FileNotFoundError:
    # fallback when installing from source package
    readme = ''

setup(
    name='{{ cookiecutter.repo_name }}',
    version=open(os.path.join('{{ cookiecutter.repo_name }}', 'VERSION')).read().strip(),
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    package_data={'{{ cookiecutter.repo_name }}': ['VERSION']},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
