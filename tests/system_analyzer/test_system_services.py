import pytest
from unittest.mock import patch
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.schemas.system_services import BaseSingleSystemService, ListSystemService
from src.system_analyzer.system_services import SystemServicesCollector


@pytest.mark.parametrize("expected_mock_output, expected_services", [
    ("""UNIT                        LOAD   ACTIVE SUB     DESCRIPTION                 
  service1     loaded active running Desc
  service2               loaded active stopped Desc
  service3        loaded active running  Desc

    LOAD   = Reflects whether the unit definition was properly loaded.
    ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
    SUB    = The low-level unit activation state, values depend on unit type.
    77 loaded units listed. Pass --all to see loaded but inactive units, too.
    To show all installed unit files use 'systemctl list-unit-files'.
""",
     ListSystemService(items=[
         BaseSingleSystemService(name="service1", status="running"),
         BaseSingleSystemService(name="service2", status="stopped"),
         BaseSingleSystemService(name="service3", status="running")
     ])

     ),
    ("""UNIT                        LOAD   ACTIVE SUB     DESCRIPTION
    service1     loaded active stopped Desc
    service2               loaded active stopped Desc
    service3        loaded active stopped  Desc
    
    LOAD   = Reflects whether the unit definition was properly loaded.
    ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
    SUB    = The low-level unit activation state, values depend on unit type.
    77 loaded units listed. Pass --all to see loaded but inactive units, too.
    To show all installed unit files use 'systemctl list-unit-files'.
    """,
     ListSystemService(items=[
         BaseSingleSystemService(name="service1", status="stopped"),
         BaseSingleSystemService(name="service2", status="stopped"),
         BaseSingleSystemService(name="service3", status="stopped")
     ]))
])
def test_system_services_collector(expected_mock_output, expected_services):
    """
    Test the functionality of the SystemServicesCollector#collect method.

    This test verifies that the SystemServicesCollector#collect method correctly collects system services by mocking
    the behavior of the ShellCommandsExecutor#execute method.

    The expected output of the mocked ShellCommandsExecutor#execute method is a string representing the output of a
    shell command that lists system services. This output is then used to create an expected ListSystemService object.

    The SystemServicesCollector#collect method is called and the returned services are compared with the expected
    services using the assert statement.

    If the test passes, it indicates that the SystemServicesCollector#collect method is correctly collecting system
    services.

    """

    with patch.object(ShellCommandsExecutor, 'execute', return_value=expected_mock_output):
        services = SystemServicesCollector().collect()
        assert services == expected_services
