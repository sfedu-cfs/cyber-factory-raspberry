from scapy.all import sniff
from src.network_analyzer.timings import init_timings
from src.network_analyzer.handlers.packet_handler import packet_handler


def start(iface=None):
    """
    Start sniffing packets on the specified interface or the default interface.

    Args:
        iface: The interface to sniff packets on. If None, the default interface will be used.
    """
    packet_counters = init_timings()
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
