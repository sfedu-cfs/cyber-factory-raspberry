from unittest.mock import patch

from src.schemas.hosts import SingleHost, ListHost
from src.schemas.ports import ListPort, SinglePort
from src.system_analyzer.ports import PortCollector


@patch('src.system_analyzer.hosts.HostCollector.collect')
@patch('src.system_analyzer.core.shell_commands_exec.ShellCommandsExecutor.execute')
def test_port_collector_collect(mock_execute, mock_host_collect):
    """
    Test the functionality of the PortCollector#collect method.

    This test verifies that the PortCollector#collect method correctly collects port information by mocking the behavior
    of the HostCollector#collect and ShellCommandsExecutor#execute methods.

    The mock_host_collect decorator is used to mock the return value of the HostCollector#collect method. It returns a
    ListHost object containing two SingleHost objects.

    The mock_execute decorator is used to mock the return value of the ShellCommandsExecutor#execute method. It returns
    a string containing the output of a Nmap scan.

    An instance of the PortCollector class is created. The collect method is then called.

    The expected_ports variable created with the expected result as a ListPort object. It contains four SinglePort
    objects, representing the open ports found in the Nmap scan for both IP addresses.

    The assert statement compares the returned ports with the expected_ports.

    If the test passes, it indicates that the PortCollector#collect method is correctly collecting port information.

    """
    # Mock the return value of HostCollector#collect
    mock_host_collect.return_value = ListHost(items=[
        SingleHost(ip='192.168.0.1', mac='00:11:22:33:44:55'),
        SingleHost(ip='192.168.0.2', mac='AA:BB:CC:DD:EE:FF')
    ])

    # Mock the return value of ShellCommandsExecutor#execute
    mock_execute.return_value = """
        Starting Nmap 7.80 ( https://nmap.org ) at 2021-01-01 00:00:00 UTC
        Nmap scan report for 192.168.0.1
        PORT    STATE SERVICE
        80/tcp  open  http
        443/tcp open  https
    """

    # Create an instance of PortCollector
    port_collector = PortCollector()

    # Call the collect method
    ports = port_collector.collect()

    # Assert the expected results
    expected_ports = ListPort(items=[
        SinglePort(ip='192.168.0.1', port=80, status='open', service='http', protocol='tcp'),
        SinglePort(ip='192.168.0.1', port=443, status='open', service='https', protocol='tcp'),
        SinglePort(ip='192.168.0.2', port=80, status='open', service='http', protocol='tcp'),
        SinglePort(ip='192.168.0.2', port=443, status='open', service='https', protocol='tcp'),
    ])
    assert ports == expected_ports
