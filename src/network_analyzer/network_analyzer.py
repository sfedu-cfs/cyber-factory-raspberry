import signal
from scapy.all import sniff
from src.network_analyzer.timings import init_timings
from src.network_analyzer.handlers.packet_handler import packet_handler
from src.core.log_config import logger


def start(iface=None):
    """
    Start sniffing packets on the specified interface or the default interface.

    Args:
        iface: The interface to sniff packets on. If None, the default interface will be used.
    """
    packet_counters = init_timings()

    # Global flag variable to control the loop
    running = True

    def stop_service(signal, frame):
        nonlocal running  # Access the outer "running" variable

        # Perform any necessary cleanup here
        logger.info("Stopping the service...")
        # You can add additional cleanup code if needed

        # Set the flag to False to exit the loop
        running = False

    # Register the signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, stop_service)

    try:
        while running:
            if iface:
                # sniff with defined interface
                sniff(prn=lambda x: packet_handler(x, timings=packet_counters),
                      iface=iface, store=False)
            else:
                # sniff with default interface
                sniff(prn=lambda x: packet_handler(x, timings=packet_counters),
                      store=False)
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        logger.info("Service stopped.")


if __name__ == "__main__":
    start()
