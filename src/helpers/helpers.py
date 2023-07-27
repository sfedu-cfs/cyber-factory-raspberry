from scapy.layers.l2 import Ether


def get_mac():
    return Ether().src


device_id = get_mac()
