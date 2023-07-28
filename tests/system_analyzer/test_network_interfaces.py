import pytest

from src.system_analyzer.network_interfaces import NetworkInterfaces


@pytest.fixture
def obj():
    return NetworkInterfaces()


def test_get_primary_network_interface(obj):
    print(obj.get_primary_network_interface_with_mask())


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
    result = obj.get_network_interfaces_mask()
    assert result == expected_result
