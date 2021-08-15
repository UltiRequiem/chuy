"""
Here I define the methods that help me in the core.
"""
import os
import json
import sys

from .decorators import keyboard_interrupt
from .ui import colorized_print, colorized_input, cyan, magenta, red, yellow


def get_config(configuration_file: str) -> dict:
    """
    Read the config and parse it to a Python dictionary.
    """
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except json.decoder.JSONDecodeError:
        colorized_print(" Your configuration is invalid!", red)
        sys.exit(0)
    except FileNotFoundError:
        colorized_print(" I can't find your configuration file :(", red)
        sys.exit(0)


def flatten(lst: list) -> list:
    """
    Flat a list.
    """
    return [item for sublist in lst for item in sublist]


def get_commands(config: dict) -> list:
    """
    Get a list with all the commands to execute.
    """

    commands = []

    for item in range(len(config)):
        try:
            commands.append(sys.argv[item])
        except IndexError:
            break

    if len(commands) == 1:
        list_commands(config)

        try:
            command = colorized_input("Which command do you want to run? ").split(" ")
        except KeyboardInterrupt:
            colorized_print("\n  Process interrupted!")
            sys.exit(0)

        commands.append(command)
        return flatten(commands[1::])

    return commands[1::]


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
