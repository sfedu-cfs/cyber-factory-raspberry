import signal
import multiprocessing
from scapy.all import sniff
from src.network_analyzer.timings import init_timings
from src.network_analyzer.handlers.packet_handler import packet_handler
from src.core.log_config import logger


def sniff_packets(packet_counters, iface=None, filter_p=None):
    """
    Sniff packets on the specified interface or the default interface.

    Args:
        filter_p:
        packet_counters: Containers for packet counters.
        iface: The interface to sniff packets on. If None, the default interface will be used.
    """
    if iface:
        # sniff with defined interface
        sniff(prn=lambda x: packet_handler(x, timings=packet_counters),
              iface=iface, filter=filter_p, store=False)
    else:
        # sniff with default interface
        sniff(prn=lambda x: packet_handler(x, timings=packet_counters),
              filter=filter_p, store=False)


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
        nonlocal running
        running = False

    # Register the signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, stop_service)

    try:
        while running:
            if iface:
                # sniff with defined interface
                core_one = multiprocessing.Process(target=sniff_packets, args=(packet_counters, iface, "port 502"))
                core_one.start()

                core_two = multiprocessing.Process(target=sniff_packets, args=(packet_counters, iface, "not port 502"))
                core_two.start()
            else:
                core_one = multiprocessing.Process(target=sniff_packets, args=(packet_counters, None, "port 502"))
                core_one.start()

                core_two = multiprocessing.Process(target=sniff_packets, args=(packet_counters, None, "not port 502"))
                core_two.start()

            # Wait for the child processes to finish or terminate them if the main process is terminated
            while running:
                if not core_one.is_alive() and not core_two.is_alive():
                    break

    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        # Terminate the child processes if they are still running
        if core_one.is_alive():
            core_one.terminate()
        if core_two.is_alive():
            core_two.terminate()

        logger.info("Service stopped.")


if __name__ == "__main__":
    start()
