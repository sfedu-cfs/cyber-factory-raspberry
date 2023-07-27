from scapy.all import *
from handlers import timings, packet_handler


def start(iface=None):
    packet_counters = timings()
    if iface:
        # sniff with defined interface
        sniff(prn=lambda x: packet_handler(x, timings=packet_counters), 
              iface=iface, store=False)
    else:
        # sniff with default interface
        sniff(prn=lambda x: packet_handler(x, timings=packet_counters), 
              store=False)
    
    
if __name__ == "__main__":
    start()
    