import pytest

from src.system_analyzer.network_interfaces import NetworkInterfaces


def test_parse_list_network_interface():
    list_network_interface = ["eth0 192.168.1.100", "eth1 192.168.1.101"]
    expected_result = [
        {"name": "eth0", "ipAddress": "192.168.1.100"},
        {"name": "eth1", "ipAddress": "192.168.1.101"}
    ]
    result = NetworkInterfaces.parse_list_network_interface(list_network_interface)
    assert result == expected_result


def test_get_primary_network_interface():
    print(NetworkInterfaces.get_primary_network_interface())
