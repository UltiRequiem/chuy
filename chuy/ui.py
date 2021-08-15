"""
Here I define everything related to Colorama :)
"""

import sys

import colorama

# For export, and easily usage :)
cyan, red, yellow, blue, magenta = (
    colorama.Fore.CYAN,
    colorama.Fore.RED,
    colorama.Fore.YELLOW,
    colorama.Fore.BLUE,
    colorama.Fore.MAGENTA,
)


def setup_colorama() -> None:
    """
    Execute init function of Colorama. This is not necessary in Linux or Darwin.
    """
    if "win" in sys.platform:
        colorama.init()


def colorized_input(text: str, color: str = yellow) -> str:
    """
    Same as normal input, but printed with colors.
    """
    return input(f" {color}{text} ")


def colorized_print(
    text: str, color: str = red, brightness: str = colorama.Style.NORMAL, **kwargs
) -> None:
    """
    Print the text with colors.
    """
    print(f"{brightness}{color}{text}{colorama.Style.RESET_ALL}", **kwargs)
