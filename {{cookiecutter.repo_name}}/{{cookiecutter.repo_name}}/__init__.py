__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
from os.path import join, dirname
__version__ = open(join(dirname(__file__), 'VERSION')).read().strip()
