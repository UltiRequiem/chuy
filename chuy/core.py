import json
import os
import sys

# TODO: Print colorized output
from colorama import Fore, Back, Style


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except json.decoder.JSONDecodeError as invalid_config:
        raise BaseException("Your configuration is invalid!") from invalid_config
    except FileNotFoundError as file_not_found:
        raise BaseException("File does not exist!") from file_not_found


# TODO: Validate the schema
def is_valide_config(configuration: dict) -> bool:
    return True


def exec_commands(command):
    print(f" $ {command} \n")
    os.system(command)
    sys.exit()


def list_commands(config: dict):
    print("Proyect Commands:")
    for item in config:
        print(
            f"""
  - {item}
      $ {config[item]}
        """
        )

    command = input("Which command do you want to run? ").lower()
    try:
        exec_commands(config[command])
    except KeyError as command_not_exist:
        raise BaseException("That is not a valid command!") from command_not_exist


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
