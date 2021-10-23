import tempfile

from chuy.helpers import get_config

def test_get_config_opens_file():
    expected = {"this": "that"}
    with tempfile.TemporaryFile(name="chuy.json") as tfile:
        fp.write(b'{"this": "that"}')
        actual = get_config(tfile.name)

    assert expected == actual 