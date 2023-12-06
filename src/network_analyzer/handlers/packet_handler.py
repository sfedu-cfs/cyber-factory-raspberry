import scapy.contrib.modbus as mb
from scapy.layers.http import HTTPRequest, HTTPResponse
from scapy.layers.l2 import Ether

from src.network_analyzer.wrappers.packet_wrappers import modbus_wrapper, arp, ipv4, ipv6, unknown_ether, reset_counter
from src.services.cyber_factory_service import CyberFactoryService
from src.helpers.helpers import get_current_time
from src.core.log_config import logger
from src.database.dao.count_packet_dao import count_packets_dao

ETHER_NUMS = {2054: arp, 2048: ipv4, 34525: ipv6}
MODBUS_LAYERS = {
    mb.ModbusADURequest: lambda p: str(p[mb.ModbusADURequest]).split(' / ')[1],
    mb.ModbusADUResponse: lambda p: str(p[mb.ModbusADUResponse]).split(' / ')[1]
}
HTTP_LAYERS = {
    HTTPRequest: lambda c: setattr(c, 'http_request_count', c.http_request_count + 1),
    HTTPResponse: lambda c: setattr(c, 'http_response_count', c.http_response_count + 1)
}

service = CyberFactoryService()


def send_to_server(output):
    current_time = get_current_time()
    last_update_time = output.last_update
    diff_seconds = (current_time.hour - last_update_time.hour) * 3600 + (
            current_time.minute - last_update_time.minute) * 60 + (current_time.second - last_update_time.second)

    if diff_seconds > output.timing or (diff_seconds < 0 and diff_seconds + 86400 > output.timing):
        service.send_count_packets(output.model_dump(by_alias=True))
        reset_counter(output)
        output.last_update = get_current_time()
    else:
        if diff_seconds not in range(0, 3601):
            logger.debug(
                f"diff_seconds: {diff_seconds}, output.timing: {output.timing}, last_update_time: {last_update_time},"
                f"current_time: {current_time}")
        if diff_seconds in range(3601, 4001):
            logger.debug(f"diff_seconds:{diff_seconds}, output.timing: {output.timing}. We in range 3601 and 4001")


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
    try:
        if ether_nums is None:
            ether_nums = ETHER_NUMS

        for counter in timings:
            # counter.last_update = get_current_time()
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

            output = counter

            send_to_server(output)
            count_packets_dao.create_count_packets(output.model_dump())

    except IndexError:
        logger.error(f"Error in packet:{packet}.")

