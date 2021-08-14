from chuy.core import is_valide_config

VALID_CONFIG = {
    "format": "poetry run black .",
    "lint": "poetry run pylint chuy tests",
    "test": "poetry run pytest",
    "package": "poetry build && poetry publish",
}

INVALID_CONFIG = {
    "format": "poetry run black .",
    "package": {"Hi": "Error", "Two": 2},
    "dependencies": {"one": "two"},
}


def test_is_valid_config():
    assert is_valide_config(
        VALID_CONFIG
    ), "Something is wrong with the function that validates the config or the schema has change!"
