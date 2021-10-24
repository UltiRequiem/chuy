"""
Core Helpers.
"""

import os
import json
import sys
import pathlib
from textwrap import dedent

import toml
from colores import colorized_print, colorized_input, CYAN, MAGENTA, YELLOW

from chuy.exceptions import InvalidChuyConfiguration, EmptyChuyConfiguration


def get_config_file(posible_config_files: list) -> str:

    for file in posible_config_files:
        if pathlib.Path(file).is_file():
            return file

    raise FileNotFoundError("Configuration file not found :(")


def get_config(file: str) -> dict:
    """
    Read the config and parse it to a Python dictionary.
    """
    config_object = {}

    with open(file=file, mode="r", encoding="utf-8") as configuration:
        try:
            if file.endswith("chuy.json"):
                config_object = json.load(configuration)
            elif file.endswith("chuy.toml"):
                config_object = toml.load(configuration)["chuy"]
            elif file.endswith("pyproject.toml"):
                config_object = toml.load(configuration)["tool"]["chuy"]
        except Exception as decodig_execption:
            raise InvalidChuyConfiguration(
                f"Error while loading {file}: {decodig_execption}"
            ) from decodig_execption

    return config_object


def list_commands(config: dict) -> None:
    """
    Print all the aliases defined in the config and their respective command.
    """
    colorized_print(" Project Commands:", CYAN)

    for item in config:
        command_str = dedent(
            f"""
                - {item}
                {YELLOW}$ {MAGENTA}{config[item]}
            """
        )
        colorized_print(command_str)


def get_commands(config: dict) -> list:
    """
    Get a list with all the commands to execute.
    """
    if not config:
        raise EmptyChuyConfiguration("There are no commands in the chuy configuration!")

    print(sys.argv)
    if len(sys.argv) == 1:
        list_commands(config)
        return colorized_input("Which command do you want to run? ").split(" ")

    commands = []
    for idx, _ in enumerate(config, start=1):
        try:
            commands.append(sys.argv[idx])
        except IndexError:
            break

    return commands


def exec_commands(command: str) -> None:
    """
    Print command with colors and then execute it.
    """
    colorized_print(f" $ {command} \n", MAGENTA)
    os.system(command)
