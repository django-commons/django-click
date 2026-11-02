"""
Support click in Django management commands.
"""

import click
from click import *  # NOQA
from .adapter import CommandRegistrator as command  # type: ignore[no-redef]  # NOQA: E501
from .adapter import GroupRegistrator as group, pass_verbosity  # type: ignore[no-redef]  # NOQA: E501

# The RegEx in setup.py requires single quotes. Rather than change it, turn off Black.
# fmt: off
__version__ = '2.5.0'
__url__ = 'https://github.com/django-commons/django-click/'
__author__ = 'Jonathan Stoppani'
__email__ = 'jonathan@stoppani.name'
__license__ = 'MIT'
# fmt: on

del click
