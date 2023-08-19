from pydantic import ValidationError
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

from src.system_analyzer.network_interfaces import DEFAULT_GATEWAY_IP
from src.schemas.arp_table import SingleARP, ListARP
from src.core.log_config import logger


class ArpTableCollector:
    """
    Represents a collector for ARP table.

    This class uses a scapy library to collect IPs and MACs from the ARP table.
    It parses the output of the scapy request and creates instances of the SingleARP class for each ARP table entry.
    The collected entries are stored in a ListARP object.

    Attributes:
        ip (str): The IP address for which to retrieve the ARP table.

    Example usage:
        arp_table = ArpTableCollector().collect()
        print(arp_table.model_dump_json(by_alias=True)
    """

    def __init__(self):
        """
        Initializes an instance of the ArpTableCollector class with the default gateway IP address.
        """
        self.ip = DEFAULT_GATEWAY_IP

    def collect(self):
        """
        Collect the ARP entries for the default gateway IP address.

        Returns:
            ListARP: A list of SingleARP instances representing the IP and MAC addresses in the ARP table.
        """
        try:
            request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=self.ip)
            answers_packets, _ = srp(request, timeout=2, retry=1)
            arp_entries = ListARP(
                items=[
                    SingleARP(ip=received.psrc, mac=received.hwsrc) for sent, received in answers_packets
                ]
            )
        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting ARP table: {e}")
            raise e

        return arp_entries
