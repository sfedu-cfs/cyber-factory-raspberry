from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sr1, srp

from src.system_analyzer.network_interfaces import DEFAULT_GATEWAY_IP
from src.schemas.arp_table import SingleARP, ListARP


class ArpTable:
    """
    ArpTable class retrieves the ARP table for a given IP address.

    Attributes:
        ip (str): The IP address for which to retrieve the ARP table.

    Methods:
        get_arp_table(): Retrieves the ARP table and returns a list of dictionaries containing IP and MAC addresses.

    Usage:
        arp_table = ArpTable()
        result = arp_table.get_arp_table()
        print(result)
    """

    def __init__(self):
        """
        Initializes an instance of the ArpTable class with the default gateway IP address.
        """
        self.ip = DEFAULT_GATEWAY_IP

    def get_arp_table(self):
        """
        Retrieves the ARP table for the specified IP address.

        Returns:
            list: A list of dictionaries containing IP and MAC addresses in the ARP table.
        """
        request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=self.ip)
        answers_packets, unanswered_packets = srp(request, timeout=2, retry=1)
        return ListARP(
            items=[
                SingleARP(ip=received.psrc, mac=received.hwsrc) for sent, received in answers_packets
            ]
        )


at = ArpTable()
arp_table = at.get_arp_table()
