import socket
import netifaces

from scapy.layers.l2 import Ether
from datetime import datetime as dt


def get_mac():
    return str(Ether().src).upper()


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def get_ip_iface(ip):
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        ifaddresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in ifaddresses:
            addresses = ifaddresses[netifaces.AF_INET]
            for address in addresses:
                if address['addr'] == ip:
                    return interface


def get_current_time():
    return dt.now().time()
