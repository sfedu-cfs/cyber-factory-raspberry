import re

from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

from src.core.log_config import logger


# TODO: Add a class with increase, decrease, and reset methods for each counter

def reset_counter(counter):
    counter.all_proto_count = 0
    counter.arp_count = 0
    counter.tcp_count = 0
    counter.udp_count = 0
    counter.icmp_count = 0
    counter.http_request_count = 0
    counter.http_response_count = 0
    counter.modbus_01_request_count = 0
    counter.modbus_01_response_count = 0
    counter.modbus_02_request_count = 0
    counter.modbus_02_response_count = 0
    counter.modbus_03_request_count = 0
    counter.modbus_03_response_count = 0
    counter.modbus_04_request_count = 0
    counter.modbus_04_response_count = 0
    counter.modbus_05_request_count = 0
    counter.modbus_05_response_count = 0
    counter.modbus_06_request_count = 0
    counter.modbus_06_response_count = 0
    counter.modbus_15_request_count = 0
    counter.modbus_15_response_count = 0
    counter.modbus_16_request_count = 0
    counter.modbus_16_response_count = 0

def tcp(packet, counter):
    """
    Increment the TCP count in the counter object.

    Args:
        packet: The packet being processed.
        counter: The counter object to update.
    """
    counter.tcp_count += 1


def udp(packet, counter):
    """
    Increment the UDP count in the counter object.

    Args:
        packet: The packet being processed.
        counter: The counter object to update.
    """
    counter.udp_count += 1


def icmp(packet, counter):
    """
    Increment the ICMP count in the counter object.

    Args:
        packet: The packet being processed.
        counter: The counter object to update.
    """
    counter.icmp_count += 1


def unknown_transport(packet, counter):
    """
    Log that an unknown transport type was encountered.

    Args:
        packet: The packet being processed.
        counter: The counter object.
    """
    logger.info(f"Unknown transport type {packet}")


def arp(packet, counter):
    """
    Increment the ARP count in the counter object.

    Args:
        packet: The packet being processed.
        counter: The counter object to update.
    """
    counter.arp_count += 1


def process_transport(packet, counter, proto_getter):
    """
    Process transport-layer packets (TCP, UDP, ICMP).
    """
    transport_nums = {6: tcp, 17: udp, 1: icmp}
    transport_layer = transport_nums.get(proto_getter(packet), unknown_transport)
    transport_layer(packet, counter)


def ipv4(packet, counter):
    """
    Process an IPv4 packet.
    """
    process_transport(packet, counter, lambda p: p[IP].proto)


def ipv6(packet, counter):
    """
    Process an IPv6 packet.
    """
    process_transport(packet, counter, lambda p: p[IPv6].nh)


def unknown_ether(packet, counter):
    """
    Log that an unknown ether type was encountered.

    Args:
        packet: The packet being processed.
        counter: The counter object.
    """
    logger.info(f"Unknown ether type {packet}")


def modbus_wrapper(packet, counter, modbus_type):
    """
    Process a Modbus packet and update the counter object.

    Args:
        packet: The packet being processed.
        counter: The counter object to update.
        modbus_type: The type of the Modbus packet.
    """
    pattern = re.compile(r"([A-Za-z])+([A-Za-z0-9]{2})", re.IGNORECASE)
    f_code = pattern.search(modbus_type).group(2)
    f_code = int(f_code, 16)

    attribute_suffix = 'request' if 'Request' in modbus_type else 'response'
    attribute_name = f'modbus_{f_code:02}_{attribute_suffix}_count'

    current_value = getattr(counter, attribute_name, 0)
    setattr(counter, attribute_name, current_value + 1)
