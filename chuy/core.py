import json
import os
import sys

from colorama import Fore, Style, init

if sys.platform == "win32":
    init()


def manage_keyboard_interrumpt(func):
    def manager():
        try:
            func()
        except KeyboardInterrupt:
            print(f"\n {Fore.BLUE}Goodbye!")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    return manager


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except json.decoder.JSONDecodeError as invalid_config:
        raise BaseException("Your configuration is invalid!") from invalid_config
    except FileNotFoundError as file_not_found:
        raise BaseException("File does not exist!") from file_not_found


def print_with_color(text, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{text}{Style.RESET_ALL}", **kwargs)


# TODO: Validate the schema
def is_valide_config(configuration: dict) -> bool:
    return True


def exec_commands(command):
    print(f" $ {command} \n")
    os.system(command)
    sys.exit()


def list_commands(config: dict):
    print_with_color(" Proyect Commands:", Fore.CYAN)
    for item in config:
        print_with_color(
            f"""
  - {item}
      $ {config[item]}
        """,
            color=Fore.RED,
        )

    command = input(f" {Fore.YELLOW}Which command do you want to run? ").lower()
    try:
        exec_commands(config[command])
    except KeyError as command_not_exist:
        raise BaseException("That is not a valid command!") from command_not_exist


@manage_keyboard_interrumpt
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
