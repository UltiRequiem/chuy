import json
import sys

from .helpers import exec_commands, list_commands
from .ui import setup_colorama


setup_colorama()


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except json.decoder.JSONDecodeError as invalid_config:
        raise BaseException("Your configuration is invalid!") from invalid_config
    except FileNotFoundError as file_not_found:
        raise BaseException("File does not exist!") from file_not_found


def main() -> None:
    config = get_config("chuy.json")

    try:
        param = sys.argv[1]
    except IndexError:
        param = list_commands(config)

    exec_commands(config[param])


if __name__ == "__main__":
    main()
