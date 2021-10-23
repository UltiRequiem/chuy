"""
Metadata Package Tests.
"""

from chuy import __package_name__, __url__, __version__, __author_email__


def test_version():
    assert isinstance(__version__, str), "The version value is invalid!"


def test_url():
    assert isinstance(__url__, str), "The URL value is invalid!"


def test_name():
    assert isinstance(__package_name__, str), "The package name value is invalid!"


def test_email():
    assert isinstance(__author_email__, str), "The email value is invalid!"
