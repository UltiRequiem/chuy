import sys
from typing import Callable

from .ui import colorized_print, red


def keyboard_interrupt(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            colorized_print("\n  Process interrupted!", red)
            sys.exit(0)

    return wrapper
