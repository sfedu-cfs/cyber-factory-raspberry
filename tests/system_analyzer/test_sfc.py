import pytest

from unittest.mock import patch

from src.system_analyzer.sfc import SFCCollector
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.schemas.sfc import ListSFC, BaseSingleSFC


@pytest.mark.parametrize("expected_mock_output, expected_sfc", [
    ("Application1\t1.0\nApplication2\t2.0\n",
     ListSFC(items=[BaseSingleSFC(name="Application1", version="1.0"),
                    BaseSingleSFC(name="Application2", version="2.0")])
     ),
    ("", ListSFC(items=[]))
])
def test_collect_applications(expected_mock_output, expected_sfc):
    """
    Test the functionality of the SFCCollector#collect method.

    This test verifies that the SFCCollector#collect method correctly collects SFC (Service Function Chain) information
    by mocking the behavior of the ShellCommandsExecutor#execute method.

    The expected_mock_output parameter represents the expected output of the ShellCommandsExecutor#execute method.

    The expected_sfc parameter represents the expected result as a ListSFC object.

    The patch.object decorator is used to mock the return value of the ShellCommandsExecutor#execute method. It returns
    the expected_mock_output.

    An instance of the SFCCollector class is created. The collect method is then called.

    The assert statement compares the returned SFC with the expected_sfc.

    If the test passes, it indicates that the SFCCollector#collect method is correctly collecting SFC information.

    """
    with patch.object(ShellCommandsExecutor, 'execute', return_value=expected_mock_output):
        sfc = SFCCollector().collect()
        assert sfc == expected_sfc
