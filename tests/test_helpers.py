"""
Chuy Helpers Tests.
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import toml

from chuy.exceptions import InvalidChuyConfiguration, EmptyChuyConfiguration
from chuy.helpers import get_config_file, get_config, list_commands, get_commands

SAMPLE_CONFIG = {"this": "that"}


def test_get_config_file_returns_file():
    with tempfile.TemporaryFile() as tfile:
        actual = get_config_file(["inexistent.json", tfile.name, "inexistent.json"])
        assert actual == tfile.name


def test_get_config_file_raises_error():
    with pytest.raises(FileNotFoundError):
        _ = get_config_file(["inexistent.json"])


@pytest.mark.parametrize(
    "filename,content",
    [
        ("chuy.json", json.dumps(SAMPLE_CONFIG)),
        ("chuy.toml", toml.dumps({"chuy": SAMPLE_CONFIG})),
        ("pyproject.toml", toml.dumps({"tool": {"chuy": SAMPLE_CONFIG}})),
    ],
)
def test_get_config_opens_file(filename, content):
    with tempfile.TemporaryDirectory() as tdir:
        filepath = Path(tdir) / filename
        with open(filepath, "w", encoding="utf8") as filehandler:
            filehandler.write(content)
        actual = get_config(str(filepath))

    assert actual == SAMPLE_CONFIG


def test_get_config_raises_invalid_config_exception():
    with tempfile.TemporaryDirectory() as tdir:
        filepath = Path(tdir) / "chuy.json"
        with open(filepath, "w", encoding="utf8") as filehandler:
            filehandler.write('{"a": _invalid_json_}')
        with pytest.raises(InvalidChuyConfiguration):
            _ = get_config(str(filepath))


@patch("chuy.helpers.colorized_print")
def test_list_commands(mocked_colorized_print):
    list_commands(SAMPLE_CONFIG)

    call_args = [i.args for i in mocked_colorized_print.call_args_list]
    assert call_args[0][0] == " Project Commands:"
    assert call_args[1][0].startswith("\n- this\n")
    assert "that\n" in call_args[1][0]


def test_get_commands_raises_empty_config_error():
    with pytest.raises(EmptyChuyConfiguration):
        _ = get_commands({})


SAMPLE_FILEPATH = "path/to/chuy/__main__.py"
SAMPLE_USER_INPUT = "my_cmd my_cmd2"


@pytest.mark.parametrize(
    "argv, expected",
    [
        pytest.param(
            [SAMPLE_FILEPATH], SAMPLE_USER_INPUT.split(" "), id="no command passed"
        ),
        pytest.param([SAMPLE_FILEPATH, "cmd1"], ["cmd1"], id="single command passed"),
        pytest.param(
            [SAMPLE_FILEPATH, "cmd1", "cmd2"],
            ["cmd1", "cmd2"],
            id="# commands = # config commands",
        ),
        pytest.param(
            [SAMPLE_FILEPATH, "cmd1", "cmd2", "cmd3"],
            ["cmd1", "cmd2"],
            id="more command than config command",
        ),
    ],
)
@patch("chuy.helpers.colorized_input")
@patch("chuy.helpers.sys")
def test_get_commands(
    mock_sys,
    mock_colorized_input,
    argv,
    expected,
):
    sample_chuy_config = {"a": "a", "b": "b"}
    mock_sys.argv = argv
    mock_colorized_input.return_value = SAMPLE_USER_INPUT
    actual = get_commands(sample_chuy_config)
    assert actual == expected
