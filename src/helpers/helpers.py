from scapy.layers.l2 import Ether


def get_mac():
    return str(Ether().src).upper()


device_id = get_mac()
