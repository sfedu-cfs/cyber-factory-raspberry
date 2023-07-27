from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sr1, srp


class ScapyWrapper:

    @staticmethod
    def get_arp_table(ip):
        request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        answers_packets, unanswered_packets = srp(request, timeout=2, retry=1)
        result = [
            {
                "ip_address": received.psrc,
                "mac_address": received.hwsrc,
            }
            for sent, received in answers_packets
        ]
        return result
