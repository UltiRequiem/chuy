from typing import Callable
from os import system as execute
from sys import exit as sys_exit

from .ui import colorized_print, colorized_input, red, cyan, yellow, magenta


def keyboard_interrupt(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            colorized_print("\n  Process interrupted!", red)
            sys_exit(0)

    return wrapper


@keyboard_interrupt
def list_commands(config: dict) -> str:
    colorized_print(" Proyect Commands:", cyan)
    for item in config:
        colorized_print(
            f"""
  - {item}
      {yellow}$ {magenta}{config[item]}
        """,
            red,
        )

    return colorized_input(f" {yellow}Which command do you want to run? ").lower()


@keyboard_interrupt
def exec_commands(command: str) -> None:
    """
    Print command with colors and then execute it
    """
    colorized_print(f" $ {command} \n", magenta)
    execute(command)
