import pytest

from unittest.mock import patch

from src.system_analyzer.connections import ConnectionsCollector
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.schemas.connections import ListConnection, BaseSingleConnection
from src.helpers.helpers import get_mac


@pytest.mark.parametrize("expected_mock_output, expected_connections", [
    (("Активные соединения с интернетом (servers and established) \n"
      "Proto Recv-Q Send-Q Local Address Foreign Address State       PID/Program name \n"
      "tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      - \n"
      "tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      - \n"
      "tcp        0      0 0.0.0.0:902             0.0.0.0:*               LISTEN      - \n"
      "tcp        0      0 127.0.0.1:32827         0.0.0.0:*               LISTEN      7500/app.asar\n"
      "tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      - \n"
      ),
     ListConnection(items=[BaseSingleConnection(protocol="tcp", src_ip_address="127.0.0.1",
                                                src_port=631, dst_ip_address="0.0.0.0", dst_port=0,
                                                state="LISTEN", service_name="-"),
                           BaseSingleConnection(protocol="tcp", src_ip_address="0.0.0.0",
                                                src_port=22, dst_ip_address="0.0.0.0", dst_port=0,
                                                state="LISTEN", service_name="-"),
                           BaseSingleConnection(protocol="tcp", src_ip_address="0.0.0.0",
                                                src_port=902, dst_ip_address="0.0.0.0", dst_port=0,
                                                state="LISTEN", service_name="-"),
                           BaseSingleConnection(protocol="tcp", src_ip_address="127.0.0.1",
                                                src_port=32827, dst_ip_address="0.0.0.0", dst_port=0,
                                                state="LISTEN", service_name="7500/app.asar"),
                           BaseSingleConnection(protocol="tcp", src_ip_address="127.0.0.53",
                                                src_port=53, dst_ip_address="0.0.0.0", dst_port=0,
                                                state="LISTEN", service_name="-")])
     )]
                         )
def test_collect_hosts(expected_mock_output, expected_connections):
    """
    Test the functionality of the ConnectionsCollector

    This test verifies that the ConnectionsCollector#collect method correctly collects connections by mocking the
    behavior of the ShellCommandsExecutor

    The test uses the pytest.mark.parametrize decorator to define multiple test cases with different expected mock
    outputs and expected connections.

    For each test case, the ShellCommandsExecutor#execute method is mocked to return the expected mock output. The
    ConnectionsCollector#collect method is then called, and the returned connections are compared with the expected
    connections using the assert statement.

    If the test passes for all test cases, it indicates that the ConnectionsCollector#collect method is correctly
    collecting connections.
    """

    with patch.object(ShellCommandsExecutor, 'execute', return_value=expected_mock_output):
        hosts = ConnectionsCollector().collect()
        assert hosts == expected_connections
