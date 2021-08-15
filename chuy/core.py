import json
import sys

from .helpers import exec_commands, list_commands
from .ui import colorized_print, red, setup_colorama


setup_colorama()


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


def main() -> None:
    config = get_config("chuy.json")

    commands = []

    for possible_command in range(len(config) + 1):
        try:
            commands.append(sys.argv[possible_command])
        except IndexError:
            break

    if len(commands) <= 1:
        commands.append(list_commands(config))

    del commands[0]

    for command in commands:
        try:
            exec_commands(config[command])
        except KeyError:
            colorized_print("  That command is not defined in your configuration!", red)


if __name__ == "__main__":
    main()
