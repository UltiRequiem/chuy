import tempfile
import json
import toml
import pytest
from pathlib import Path
from chuy.helpers import get_config

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
