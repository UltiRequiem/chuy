from sys import platform

from colorama import Fore, Style, init

cyan, red, yellow, blue = Fore.CYAN, Fore.RED, Fore.YELLOW, Fore.BLUE

reset_style = Style.NORMAL


def setup_colorama() -> None:
    """
    This is not necessary in Linux or Darwin
    """
    if platform in ["win32", "cygwin"]:
        init()


def colorized_input(text: str, color: str = yellow) -> str:
    """
    Return the input, but the input is printed with colors
    """
    return input(f" {color}{text} ")


def colorized_print(
    text: str, color: str = blue, brightness: str = reset_style, **kwargs
) -> None:
    """
    Print the text colorized
    """
    print(f"{brightness}{color}{text}{Style.RESET_ALL}", **kwargs)
