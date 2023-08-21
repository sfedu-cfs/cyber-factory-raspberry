import scapy.contrib.modbus as mb
from datetime import datetime as dt
from scapy.layers.l2 import Ether
from scapy.layers.http import HTTPRequest, HTTPResponse
from src.network_analyzer.wrappers.packet_wrappers import modbus_wrapper, arp, ipv4, ipv6, unknown_ether

ETHER_NUMS = {2054: arp, 2048: ipv4, 34525: ipv6}
MODBUS_LAYERS = {
    mb.ModbusADURequest: lambda p: str(p[mb.ModbusADURequest]).split(' / ')[1],
    mb.ModbusADUResponse: lambda p: str(p[mb.ModbusADUResponse]).split(' / ')[1]
}
HTTP_LAYERS = {
    HTTPRequest: lambda c: setattr(c, 'http_request_count', c.http_request_count + 1),
    HTTPResponse: lambda c: setattr(c, 'http_response_count', c.http_response_count + 1)
}


def packet_handler(packet, timings, ether_nums=None):
    """
    Handle a packet and update the timings.

    Args:
        packet: The packet being processed.
        timings: The timings object to update.
        ether_nums: A dictionary of ether types and their corresponding functions.

    Returns:
        The output string containing the model dump JSON.
    """
    if ether_nums is None:
        ether_nums = ETHER_NUMS
    output = ""

    for counter in timings:
        counter.last_update = dt.now().time()
        counter.all_proto_count += 1

        # Ether handling
        ether = ether_nums.get(packet[Ether].type, unknown_ether)
        ether(packet, counter)

        # Modbus handling
        for layer, extractor in MODBUS_LAYERS.items():
            if layer in packet:
                modbus_type = extractor(packet)
                modbus_wrapper(packet, counter, modbus_type)

        # HTTP handling
        for layer, action in HTTP_LAYERS.items():
            if packet.haslayer(layer):
                action(counter)

        output += counter.model_dump_json(indent=4)

    return output
