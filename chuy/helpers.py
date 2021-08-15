"""
Here I define the methods that help me in the core.
"""
import os
import json
import sys

from .decorators import keyboard_interrupt
from .ui import colorized_print, cyan, magenta, red, yellow


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except json.decoder.JSONDecodeError:
        colorized_print(" Your configuration is invalid!", red)
        sys.exit(0)
    except FileNotFoundError:
        colorized_print(" I can't find your configuration file :(", red)
        sys.exit(0)


@keyboard_interrupt
def list_commands(config: dict) -> None:
    """
    Print all the aliases defined in the config and their respective command.
    """
    colorized_print(" Project Commands:", cyan)

    for item in config:
        colorized_print(
            f"""
  - {item}
      {yellow}$ {magenta}{config[item]}
        """,
            red,
        )


@keyboard_interrupt
def exec_commands(command: str) -> None:
    """
    Print command with colors and then execute it.
    """
    colorized_print(f" $ {command} \n", magenta)
    os.system(command)
