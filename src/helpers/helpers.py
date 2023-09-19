from scapy.layers.l2 import Ether
from datetime import datetime as dt


def get_mac():
    return str(Ether().src).upper()


def get_current_time():
    return dt.now().time()
