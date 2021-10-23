import tempfile
from unittest.mock import patch
import json
import toml
import pytest
from pathlib import Path
from chuy.helpers import get_config, list_commands

SAMPLE_CONFIG = {"this": "that"}


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
        fp = Path(tdir) / filename
        with open(fp, "w") as f:
            f.write(content)
        actual = get_config(str(fp))

    assert actual == SAMPLE_CONFIG


@patch("chuy.helpers.colorized_print")
def test_list_commands(mocked_colorized_print):
    list_commands(SAMPLE_CONFIG)

    call_args = [i.args for i in mocked_colorized_print.call_args_list]
    assert call_args[0][0] == " Project Commands:"
    assert call_args[1][0].startswith("\n  - this\n")
    assert "that\n" in call_args[1][0]