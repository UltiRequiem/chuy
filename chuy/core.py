import json
import sys

from .helpers import exec_commands, list_commands
from .ui import setup_colorama


setup_colorama()


def is_valide_config(configuration: dict) -> bool:
    return bool(configuration)


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except json.decoder.JSONDecodeError as invalid_config:
        raise BaseException("Your configuration is invalid!") from invalid_config
    except FileNotFoundError as file_not_found:
        raise BaseException("File does not exist!") from file_not_found


def main():
    config = get_config("chuy.json")

    try:
        param = sys.argv[1]
    except IndexError:
        list_commands(config)

    if is_valide_config(config):
        exec_commands(config[param])


if __name__ == "__main__":
    main()
