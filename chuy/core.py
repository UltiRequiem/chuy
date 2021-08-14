import json
import os
from sys import argv


def get_config(configuration_file: str) -> dict:
    try:
        with open(configuration_file, "r") as reader:
            return json.load(reader)
    except ValueError:
        raise BaseException("Your configuration is invalid!")
    except FileNotFoundError:
        raise BaseException("File does not exist!")


def is_valide_config(configuration: dict) -> bool:
    return True


def exec_commands(command):
    print(f" $ {command} \n")
    os.system(command)


def list_commands(config: dict):
    print("Proyect Commands:")
    for item in config:
        print(item)

    exit()


def main():
    config = get_config("chuy.json")

    try:
        param = argv[1]
    except IndexError:
        list_commands(config)

    if is_valide_config(config):
        exec_commands(config[param])


if __name__ == "__main__":
    main()
