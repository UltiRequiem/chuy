import sys
import typing

from .ui import colorized_print


def keyboard_interrupt(func: typing.Callable) -> typing.Callable:
    """
    This makes the traceback not printed.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            colorized_print("\n  Process interrupted!")
            sys.exit(0)

    return wrapper
