"""
Chuy Entry Point
"""

from colores import error_no_traceback, setup_colorama
from .exceptions import UndefinedChuyCommand
from .helpers import exec_commands, get_commands, get_config, get_config_file


def entry_point() -> None:
    """
    Chuy entry point
    """

    setup_colorama()

    config = get_config(get_config_file(["chuy.json", "pyproject.toml", "chuy.toml"]))
    commands = get_commands(config)
    invalid_commands = set(commands).difference(set(config))
    if invalid_commands:
        raise UndefinedChuyCommand(
            f"These commands are not defined in your configuration: {invalid_commands}"
        )

    for command in commands:
        exec_commands(config[command])


def main():
    """
    General 'try, catch' as handler
    """
    try:
        entry_point()
    except KeyboardInterrupt:
        error_no_traceback("\nProcess killed by the user!")
    except Exception as err:  # pylint: disable=broad-except
        error_no_traceback(str(err))


if __name__ == "__main__":
    main()
