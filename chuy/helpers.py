import os

from .decorators import keyboard_interrupt
from .ui import colorized_input, colorized_print, cyan, magenta, red, yellow


@keyboard_interrupt
def list_commands(config: dict) -> str:
    colorized_print(" Project Commands:", cyan)
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
    os.system(command)
