from unittest.mock import patch

import pytest
from scapy.layers.l2 import Ether, ARP

from src.schemas.arp_table import SingleARP, ListARP
from src.system_analyzer.arp_table import ArpTableCollector


@pytest.mark.parametrize("mock_response, expected_arp_table", [
    ([
        (Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.1"), ARP(psrc="192.168.1.1", hwsrc="00:11:22:33:44:55")),
        (Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.2"), ARP(psrc="192.168.1.2", hwsrc="AA:BB:CC:DD:EE:FF")),
    ], ListARP(
        items=[
            SingleARP(ip="192.168.1.1", mac="00:11:22:33:44:55"),
            SingleARP(ip="192.168.1.2", mac="AA:BB:CC:DD:EE:FF"),
        ]
    ))
])
def test_get_arp_table(mock_response, expected_arp_table):
    """
    Test the functionality of the ArpTableCollector.collect method.

    This test verifies that the ArpTableCollector.collect method correctly collects ARP table entries by mocking the
    behavior of the srp function from the scapy library.

    The mock_response parameter represents a list of tuples, where each tuple contains an Ethernet frame and an ARP
    packet. These packets simulate the response received from the network when performing an ARP scan.

    The expected_arp_table parameter represents the expected ARP table entries as a ListARP object.

    The srp function is patched to return the mock_response. The ArpTableCollector.collect method is then called, and
    the returned ARP table is compared with the expected ARP table using the assert statement.

    If the test passes, it indicates that the ArpTableCollector.collect method is correctly collecting ARP table entries.

    """
    with patch("src.system_analyzer.arp_table.srp", return_value=(mock_response, [])):
        at = ArpTableCollector()
        arp_table = at.collect()

    assert arp_table == expected_arp_table
