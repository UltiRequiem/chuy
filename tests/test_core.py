from subprocess import CompletedProcess, CalledProcessError
from unittest.mock import patch, Mock

import pytest

from chuy import exec_commands
from chuy.exceptions import UndefinedChuyCommand
from chuy.core import main, entry_point


def _create_exc_raising_func(exc):
    def my_func(*a, **kw):
        raise exc

    return my_func


@patch("chuy.core.get_config")
@patch("chuy.core.get_config_file")
@patch("chuy.core.get_commands")
@patch("chuy.core.exec_commands")
def test_entry_point_run_valid_command(
    mock_exec_commands, mock_get_commands, mock_get_config_file, mock_get_config
):
    mock_get_config.return_value = {"a": "b"}
    mock_get_commands.return_value = ["a"]
    entry_point()
    mock_get_config_file.assert_called()
    mock_exec_commands.assert_called_once_with("b")


@patch("chuy.core.get_config")
@patch("chuy.core.get_config_file")
@patch("chuy.core.get_commands")
def test_entry_point_raises_invalid_command_error(
    mock_get_commands, mock_get_config_file, mock_get_config
):
    mock_get_config.return_value = {"a": "b"}
    mock_get_commands.return_value = ["c"]
    with pytest.raises(UndefinedChuyCommand):
        entry_point()
    mock_get_config_file.assert_called()


@patch("chuy.core.get_config")
@patch("chuy.core.get_config_file")
@patch("chuy.core.get_commands")
@patch("chuy.core.exec_commands")
def test_entry_point_raises_invalid_command_error_before_running_any_command(
    mock_exec_commands, mock_get_commands, mock_get_config_file, mock_get_config
):
    mock_get_config.return_value = {"a": "_", "b": "_"}
    mock_get_commands.return_value = ["a", "c"]
    with pytest.raises(UndefinedChuyCommand):
        entry_point()

    mock_get_config_file.assert_called()
    assert not mock_exec_commands.called


def test_exec_commands_raises_if_a_command_returns_non_zero_status_code():
    with pytest.raises(CalledProcessError):
        exec_commands("_missing_command_")


@patch("chuy.core.entry_point")
def test_main_runs(mock_entry_point):
    main()
    mock_entry_point.assert_called_once()


@patch("chuy.core.error_no_traceback")
@patch("chuy.core.entry_point", new=_create_exc_raising_func(KeyboardInterrupt))
def test_main_catches_keyinterrupt_exceptions(mock_error_no_traceback):
    main()
    assert mock_error_no_traceback.called
    mock_error_no_traceback.assert_called_once_with("\nProcess killed by the user!")


@patch("chuy.core.error_no_traceback")
@patch("chuy.core.entry_point", new=_create_exc_raising_func(ValueError("myerr")))
def test_main_catches_other_exceptions(mock_error_no_traceback):
    main()
    assert mock_error_no_traceback.called
    mock_error_no_traceback.assert_called_once_with("myerr")
