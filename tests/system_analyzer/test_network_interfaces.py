from unittest import mock

import pytest

from src.schemas.interfaces import ListNetworkInterface, BaseSingleNetworkInterfaceMask
from src.system_analyzer.network_interfaces import NetworkInterfaces


@pytest.mark.parametrize("network_interfaces_ips, network_interfaces_names, expected_result", [
    (["eth0 192.168.1.100/24", "eth1 192.168.2.200/24"], ["eth0", "eth1"], {
        "items": [
            {"name": "eth0", "ip": "192.168.1.100/24"},
            {"name": "eth1", "ip": "192.168.2.200/24"}
        ]
    }),
    (["eth0 192.168.1.100/24", "eth1 192.168.2.200/24"], ["eth0", "eth1", "eth2"], {
        "items": [
            {"name": "eth0", "ip": "192.168.1.100/24"},
            {"name": "eth1", "ip": "192.168.2.200/24"},
            {"name": "eth2"}
        ]
    }),
    (["eth0 192.168.1.100/24", "eth1 192.168.2.200/24"], ["eth0"], {
        "items": [
            {"name": "eth0", "ip": "192.168.1.100/24"},
            {"name": "eth1", "ip": "192.168.2.200/24"}
        ]
    }),
    ([], [], {"items": []})
])
def test_get_list_network_interfaces(network_interfaces_ips, network_interfaces_names, expected_result):
    ni = NetworkInterfaces()
    ni.parse_network_interfaces_data = mock.Mock(return_value=ListNetworkInterface(**expected_result))
    ni.network_interfaces_ips = network_interfaces_ips
    ni.network_interfaces_names = network_interfaces_names

    result = ni.get_list_network_interfaces()

    assert result == ListNetworkInterface(**expected_result)
    ni.parse_network_interfaces_data.assert_called_once_with(network_interfaces_ips)


@pytest.mark.parametrize("list_network_interfaces, expected_result", [
    ([
         {"name": "eth0", "ip": "192.168.1.100/24"},
         {"name": "eth1", "ip": "192.168.2.200/24"}
     ], [
         BaseSingleNetworkInterfaceMask(name="eth0", netmask="24"),
         BaseSingleNetworkInterfaceMask(name="eth1", netmask="24")
     ]),
    ([], [])
])
def test_get_network_interfaces_mask(list_network_interfaces, expected_result):
    ni = NetworkInterfaces()
    ni.get_list_network_interfaces = mock.Mock(return_value=ListNetworkInterface(items=list_network_interfaces))

    result = ni.get_network_interfaces_mask()

    assert result == expected_result
    ni.get_list_network_interfaces.assert_called_once()


@pytest.mark.parametrize("list_network_interfaces_ips, expected_result", [
    (["eth0 192.168.1.100", "eth1 192.168.2.200"], [
        {"name": "eth0", "ipAddress": "192.168.1.100"},
        {"name": "eth1", "ipAddress": "192.168.2.200"}
    ]),
    ([], [])
])
def test_parse_network_interfaces_ips(list_network_interfaces_ips, expected_result):
    ni = NetworkInterfaces()
