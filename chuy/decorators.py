import typing

from .ui import error


def keyboard_interrupt(func: typing.Callable) -> typing.Callable:
    """
    This makes the traceback not printed.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            error("\n  Process interrupted!")

    return wrapper
