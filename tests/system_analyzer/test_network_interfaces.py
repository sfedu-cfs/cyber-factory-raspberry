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
    """
    Test the functionality of the NetworkInterfaces.get_list_network_interfaces method.

    This test verifies that the get_list_network_interfaces method correctly parses network interface data and returns
    a ListNetworkInterface object.

    The network_interfaces_ips parameter represents a list of strings, where each string contains the name and IP
    address/netmask of a network interface.

    The network_interfaces_names parameter represents a list of network interface names.

    The expected_result parameter represents the expected result as a dictionary.

    The parse_network_interfaces_data method is mocked to return the expected_result. The get_list_network_interfaces
    method is then called, and the returned ListNetworkInterface object is compared with the expected result using the
    assert statement.

    If the test passes, it indicates that the get_list_network_interfaces method is correctly parsing network interface
    data and returning the expected result.

    """
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
    """
    Test the functionality of the NetworkInterfaces.get_network_interfaces_mask method.

    This test verifies that the get_network_interfaces_mask method correctly extracts the network interface names and
    netmasks from a ListNetworkInterface object and returns a list of BaseSingleNetworkInterfaceMask objects.

    The list_network_interfaces parameter represents a list of dictionaries, where each dictionary contains the name and
    IP address/netmask of a network interface.

    The expected_result parameter represents the expected result as a list of BaseSingleNetworkInterfaceMask objects.

    The get_list_network_interfaces method is mocked to return a ListNetworkInterface object with the provided
    list_network_interfaces. The get_network_interfaces_mask method is then called, and the returned list of
    BaseSingleNetworkInterfaceMask objects is compared with the expected result using the assert statement.

    If the test passes, it indicates that the get_network_interfaces_mask method is correctly extracting the network
    interface names and netmasks and returning the expected result.

    """
    ni = NetworkInterfaces()
    ni.get_list_network_interfaces = mock.Mock(return_value=ListNetworkInterface(items=list_network_interfaces))

    result = ni.get_network_interfaces_mask()

    assert result == expected_result