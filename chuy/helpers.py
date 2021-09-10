"""
Here I define the methods that help me in the core.
"""
import os
import json
import sys

import toml

from .decorators import keyboard_interrupt
from .ui import colorized_print, colorized_input, cyan, magenta, yellow, error

# codereview.stackexchange.com/questions/267841


def get_config_file() -> str:
    posible_config_files = ["chuy.json", "pyproject.toml", "chuy.toml"]

    for file in posible_config_files:
        try:
            with open(file, mode="r", encoding="utf-8"):
                return file
        except FileNotFoundError:
            continue

    error("File not Found")


def get_config(file: str) -> dict:
    """
    Read the config and parse it to a Python dictionary.
    """

    with open(file=file, mode="r", encoding="utf-8") as configuration:
        return {
            "chuy.json": json.load(configuration),
            "chuy.toml": toml.load(configuration),
            "pyproject.toml": toml.load(configuration)["tool"]["chuy"],
        }[file]


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
        """
        )


@keyboard_interrupt
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
        return colorized_input("Which command do you want to run? ").split(" ")

    return commands[1::]


@keyboard_interrupt
def exec_commands(command: str) -> None:
    """
    Print command with colors and then execute it.
    """
    colorized_print(f" $ {command} \n", magenta)
    os.system(command)
