import pytest

from unittest.mock import patch

from src.system_analyzer.hosts import HostCollector
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.schemas.hosts import ListHost, BaseHost
from src.helpers.helpers import get_mac


@pytest.mark.parametrize("expected_mock_output, expected_hosts", [
    (("Nmap scan report for 192.168.0.1\nHost is up (0.0025s latency).\nMAC Address: "
      "AA:AA:AA:AA:AA:AA (Unknown)\nNmap scan report for 192.168.0.2\nHost"
      "is up (0.020s latency).\nMAC Address: BB:BB:BB:BB:BB:BB (Unknown)"),
     ListHost(items=[BaseHost(ip="192.168.0.1", mac="AA:AA:AA:AA:AA:AA"),
                     BaseHost(ip="192.168.0.2", mac="BB:BB:BB:BB:BB:BB")])
     ),
    (("Nmap scan report for 192.168.0.1\nHost is up (0.0025s latency).\nMAC Address: "
      "AA:AA:AA:AA:AA:AA (Unknown)\nNmap scan report for 192.168.0.2\nHost"
      "is up (0.020s latency)."),
     ListHost(items=[BaseHost(ip="192.168.0.1", mac="AA:AA:AA:AA:AA:AA"),
                     BaseHost(ip="192.168.0.2", mac=get_mac())])
     ),
    ("", ListHost(items=[]))
]
)
def test_collect_hosts(expected_mock_output, expected_hosts):
    """
    Test the functionality of the HostCollector.collect method.

    This test verifies that the HostCollector.collect method correctly collects hosts by mocking the behavior of the
    ShellCommandsExecutor.execute method.

    The test uses the pytest.mark.parametrize decorator to define multiple test cases with different expected mock
    outputs and expected hosts.

    For each test case, the ShellCommandsExecutor.execute method is mocked to return the expected mock output. The
    HostCollector.collect method is then called, and the returned hosts are compared with the expected hosts using
    the assert statement.

    If the test passes for all test cases, it indicates that the HostCollector.collect method is correctly collecting
    hosts.

    """

    with patch.object(ShellCommandsExecutor, 'execute', return_value=expected_mock_output):
        hosts = HostCollector().collect()
        assert hosts == expected_hosts
