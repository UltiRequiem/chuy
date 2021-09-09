"""
This file define chuy as a module.
"""

# For plugins that have a dependency on Chuy
from .core import main
from .decorators import keyboard_interrupt
from .helpers import exec_commands, list_commands
from .ui import (
    blue,
    colorized_input,
    colorized_print,
    cyan,
    magenta,
    red,
    setup_colorama,
    yellow,
)

# Package Meta Data
__version__ = "1.3.0"
__authors__ = ["Eliaz Bobadilla <eliaz.bobadilladev@gmail.com>"]
__author_email__ = "eliaz.bobadilladev@gmail.com"
__url__ = "https://github.com/UltiRequiem/chuy"
__package_name__ = "chuy"
