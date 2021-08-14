import json
from os import system
from sys import argv


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except FileNotFoundError:
        raise BaseException("File does not exist!")


def exec_commands(config, command):
    # command = config[command]
    system(config[command])


if __name__ == "__main__":
    exec_commands(get_config("runpy.json"), argv[1])
