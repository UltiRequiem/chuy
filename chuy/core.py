from .helpers import exec_commands, get_commands, get_config
from .ui import colorized_print, setup_colorama


setup_colorama()


def main() -> None:
    config = get_config("chuy.json")

    for command in get_commands(config):
        try:
            exec_commands(config[command])
        except KeyError:
            colorized_print("  That command is not defined in your configuration!")


if __name__ == "__main__":
    main()
