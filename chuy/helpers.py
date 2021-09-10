"""
Here I define the methods that help me in the core.
"""

import os
import json
import sys
import pathlib

import toml

from colores import colorized_print, colorized_input, CYAN, MAGENTA, YELLOW


def get_config_file(posible_config_files: list) -> str:

    for file in posible_config_files:
        if pathlib.Path(file).is_file():
            return file

    raise BaseException("Configuration file not found :(")


def get_config(file: str) -> dict:
    """
    Read the config and parse it to a Python dictionary.
    """

    with open(file=file, mode="r", encoding="utf-8") as configuration:
        try:
            return {
                "chuy.json": json.load(configuration) if file == "chuy.json" else {},
                "chuy.toml": toml.load(configuration)["chuy"]
                if file == "chuy.toml"
                else {},
                "pyproject.toml": toml.load(configuration)["tool"]["chuy"]
                if file == "pyproject.toml"
                else {},
            }[file]
        except Exception as decodig_execption:
            raise BaseException(f"Error while loading {file}.") from decodig_execption


def list_commands(config: dict) -> None:
    """
    Print all the aliases defined in the config and their respective command.
    """
    colorized_print(" Project Commands:", CYAN)

    for item in config:
        colorized_print(
            f"""
  - {item}
      {YELLOW}$ {MAGENTA}{config[item]}
        """
        )


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


def exec_commands(command: str) -> None:
    """
    Print command with colors and then execute it.
    """
    colorized_print(f" $ {command} \n", MAGENTA)
    os.system(command)
