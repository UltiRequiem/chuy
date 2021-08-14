from os import system as execute
from sys import exit as sys_exit

from .ui import colorized_print, colorized_input, red, cyan, yellow, magenta


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


def exec_commands(command: str) -> None:
    """
    Print command with colors and then execute it
    """
    colorized_print(f" $ {command} \n", magenta)
    execute(command)
    sys_exit()
