import sys
import typing

from .ui import colorized_print, red


def keyboard_interrupt(func: typing.Callable) -> typing.Callable:
    """
    This makes the traceback not printed.
    """

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            colorized_print("\n  Process interrupted!", red)
            sys.exit(0)

    return wrapper
