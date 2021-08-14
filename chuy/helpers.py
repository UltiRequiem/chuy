from os import system as execute
from sys import exit as sys_exit

from .ui import colorized_print, red, cyan, yellow


def error_handler(func):
    def manager():
        try:
            func()
        except KeyboardInterrupt:
            colorized_print("Process interrupted!", red)
            sys_exit(0)
        except KeyError:
            colorized_print("That command is not in your config!", red)
            sys_exit(0)
        except Exception:
            colorized_print(
                """
            \n An error occurred!
            You can create a ticket in https://github.com/UltiRequiem/chuy/issues/new
            """,
                red,
            )
            sys_exit(0)

    return manager


def list_commands(config: dict):
    colorized_print(" Proyect Commands:", cyan)
    for item in config:
        colorized_print(
            f"""
  - {item}
      $ {config[item]}
        """,
            red,
        )

    command = input(f" {yellow}Which command do you want to run? ").lower()

    try:
        exec_commands(config[command])
        sys_exit()
    except KeyError as command_not_exist:
        raise BaseException("That is not a valid command!") from command_not_exist


def exec_commands(command: str) -> None:
    colorized_print(f" $ {command} \n")
    execute(command)
    sys_exit()
