import pytest

from unittest.mock import patch

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.schemas.apps import BaseSingleApp, ListApp
from src.system_analyzer.apps import AppsCollector


@pytest.mark.parametrize(("expected_mock_output", "expected_apps"), [
    ("app1\t1.0\tDesc1\napp2\t2.0\tDesc2\napp3\t3.0\tDesc3\n",
     ListApp(items=[BaseSingleApp(name="app1", version="1.0", description="Desc1"),
                    BaseSingleApp(name="app2", version="2.0", description="Desc2"),
                    BaseSingleApp(name="app3", version="3.0", description="Desc3")])
     ),
    ("", ListApp(items=[]))
])
def test_app_collector(expected_mock_output, expected_apps):
    """
    Test the functionality of the AppCollector.collect method.

    This test verifies that the AppCollector.collect method correctly collects apps by mocking the behavior of the
    ShellCommandsExecutor.execute method.

    The expected output of the mocked ShellCommandsExecutor.execute method is a string representing the output of a
    shell command that lists apps. This output is then used to create an expected ListApp object.

    The AppCollector.collect method is called and the returned apps are compared with the expected apps using the
    assert statement.

    If the test passes, it indicates that the AppCollector.collect method is correctly collecting apps.

    """
    with patch.object(ShellCommandsExecutor, "execute", return_value=expected_mock_output):
        apps = AppsCollector().collect()
        assert apps == expected_apps
