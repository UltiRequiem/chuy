"""
Here I define the methods that help me in the core.
"""
import os
import json
import sys

import toml

from .decorators import keyboard_interrupt
from .ui import colorized_print, colorized_input, cyan, magenta, yellow

# Time to a new post on codereview.stackexchange.com

def get_config_file() -> str:
    posible_config_files = ["chuy.json", "pyproject.toml", "chuy.toml"]

    for file in posible_config_files:
        try:
            with open(file, mode="r", encoding="utf-8"):
                return file
        except FileNotFoundError:
            continue


# FIX: NEEDS A CLEAN UP

def get_config(file: str) -> dict:
    """
    Read the config and parse it to a Python dictionary.
    """
    if file == "chuy.json":
        try:
            with open(file, mode="r", encoding="utf-8") as reader:
                return json.load(reader)
        except json.decoder.JSONDecodeError:
            colorized_print(" Your configuration is invalid!")
            sys.exit(0)
    elif file == "pyproject.toml":
        try:
            with open(file, mode="r", encoding="utf-8") as reader:
                return toml.load(reader)["tool"]["chuy"]
        except toml.TomlDecodeError:
            colorized_print(" Your configuration is invalid!")
            sys.exit(0)
    elif file == "chuy.toml":
        try:
            with open(file, mode="r", encoding="utf-8") as reader:
                return toml.load(reader)["chuy"]
        except toml.TomlDecodeError:
            colorized_print(" Your configuration is invalid!")
            sys.exit(0)
    else:
        colorized_print("File not Found")
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
