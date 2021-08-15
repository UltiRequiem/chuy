import sys

from .helpers import exec_commands, get_config, list_commands
from .ui import colorized_print, colorized_input, setup_colorama


setup_colorama()


def main() -> None:
    config = get_config("chuy.json")

    commands = []

    for item in range(len(config) + 1):
        try:
            commands.append(sys.argv[item])
        except IndexError:
            break

    if len(commands) == 1:
        list_commands(config)
        try:
            command = colorized_input("Which command do you want to run? ")
        except KeyboardInterrupt:
            colorized_print("\n  Process interrupted!")
            sys.exit(0)
        commands.append(command)

    # This contains the path of the file
    del commands[0]

    for command in commands:
        try:
            exec_commands(config[command])
        except KeyError:
            colorized_print("  That command is not defined in your configuration!")


if __name__ == "__main__":
    main()
