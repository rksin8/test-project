## Based on pep-0328

Assuming that the current file is either moduleX.py or subpackage1/__init__.py, following are correct usages of the new syntax:

from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
from ...package import bar
from ...sys import path
