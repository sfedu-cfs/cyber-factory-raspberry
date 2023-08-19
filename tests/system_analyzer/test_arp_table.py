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
    with patch("src.system_analyzer.arp_table.srp", return_value=(mock_response, [])):
        at = ArpTableCollector()
        arp_table = at.collect()

    assert arp_table == expected_arp_table

