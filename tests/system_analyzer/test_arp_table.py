import pytest

from src.system_analyzer.arp_table import ArpTable


@pytest.fixture
def obj():
    return ArpTable()


def test_get_arp_table(obj):
    list_network_interface = ["eth0 192.168.1.100", "eth1 192.168.1.101"]
    expected_result = [
        {"ipAddress": "192.168.0.100", "macAddress": "1c:bf:ce:3e:84:2e"},
        {"ipAddress": "192.168.1.102", "macAddress": "d6:31:0c:3c:c6:ed"}
    ]
    result = obj.parse_list_network_interface(list_network_interface)
    assert result == expected_result
