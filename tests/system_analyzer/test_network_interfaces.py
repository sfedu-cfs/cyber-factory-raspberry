import pytest

from src.system_analyzer.network_interfaces import NetworkInterfaces


@pytest.fixture
def obj():
    return NetworkInterfaces()


def test_parse_list_network_interface():
    list_network_interface = ["eth0 192.168.1.100", "eth1 192.168.1.101"]
    expected_result = [
        {"name": "eth0", "ipAddress": "192.168.1.100"},
        {"name": "eth1", "ipAddress": "192.168.1.101"}
    ]
    result = NetworkInterfaces.parse_list_network_interface(list_network_interface)
    print(result)
    assert result == expected_result


def test_get_primary_network_interface():
    print(NetworkInterfaces.get_primary_network_interface())


def test_get_network_interfaces(obj):
    print(obj.get_list_network_interfaces())


def test_get_network_interfaces_mask(obj):
    list_network_interface = obj.get_list_network_interfaces()
    expected_result = [
        {
            "name": "lo",
            "netmask": "8"
        },
        {
            "name": "wlp0s20f3",
            "netmask": "24"
        },
        {
            "name": "enp7s0f1",
            "netmask": None
        }
        
    ]
    result = NetworkInterfaces.get_network_interfaces_mask(list_network_interface)
    assert result == expected_result
