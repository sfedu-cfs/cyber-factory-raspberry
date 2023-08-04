import pytest

from unittest.mock import patch

from src.system_analyzer.sfc import InstalledApplications
from src.schemas.sfc import SFC
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_INSTALLED_APPLICATIONS


@pytest.fixture
def mock_shell_commands_executor():
    # Mock the ShellCommandsExecutor class to return a predefined result
    with patch.object(ShellCommandsExecutor, 'execute') as mock_execute:
        mock_execute.return_value = "Application1\t1.0\nApplication2\t2.0\n"
        yield


def test_collect_applications(mock_shell_commands_executor):
    # Create an instance of InstalledApplications
    installed_apps = InstalledApplications()

    # Call the collect method
    installed_apps.collect()

    # Assert that the applications list is populated correctly
    assert len(installed_apps.applications) == 2
    assert installed_apps.applications[0].name == "Application1"
    assert installed_apps.applications[0].version == "1.0"
    assert installed_apps.applications[1].name == "Application2"
    assert installed_apps.applications[1].version == "2.0"

