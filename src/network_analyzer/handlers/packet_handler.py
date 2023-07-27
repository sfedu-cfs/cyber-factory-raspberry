import datetime
from scapy.all import *
import scapy.contrib.modbus as mb
from scapy.layers.http import HTTPRequest, HTTPResponse
from handlers.wrappers import wrap_count_timings

def packet_handler(packet, timings):
    """
    This function work as packet handler for scapy.sniff

    Args:
        packet (scapy type): scapy layered form of internet packet
    """
    output = {
        "time": datetime.now()
    }
    if int(packet[Ether].type) == 2054: # ARP type
        output["is_arp"] = True
        wrap_count_timings(timings, output)
    if packet[Ether].type == 2048: # IPv4
        if packet[IP].proto == 6:
            output["is_tcp"] = True
        elif packet[IP].proto == 17:
            output["is_udp"] = True
        elif packet[IP].proto == 1:
            output["is_icmp"] = True
        wrap_count_timings(timings, output)
    elif packet[Ether].type == 34525: # IPv6
        if packet[IPv6].nh == 6:
            output["is_tcp"] = True
        elif packet[IPv6].nh == 17:
            output["is_udp"] = True
        elif packet[IPv6].nh == 1:
            output["is_icmp"] = True
        wrap_count_timings(timings, output)
    if mb.ModbusADURequest in packet: # Looking for ModBus layer
        modbus_type = str(packet[mb.ModbusADURequest]).split(' / ')[1]
        print()
        output["modbus_type"] = modbus_type
        wrap_count_timings(timings, output)
    elif mb.ModbusADUResponse in packet:
        modbus_type = str(packet[mb.ModbusADUResponse]).split(' / ')[1]
        output["modbus_type"] = modbus_type
        wrap_count_timings(timings, output)
    if packet.haslayer(HTTPRequest): #Looking for HTTP layer
        output["http_request"] = True
        wrap_count_timings(timings, output)
    elif packet.haslayer(HTTPResponse):
        output["http_response"] = True
        wrap_count_timings(timings, output)
    
    
        
if __name__ == "__main__":
    #print(packet_handler(Ether()/IP()/TCP()/mb.ModbusADURequest()/mb.ModbusPDU02ReadDiscreteInputsResponse()))
    print(packet_handler(Ether()/IP()/TCP()/mb.ModbusADURequest()/mb.ModbusPDU03ReadHoldingRegistersRequest()))