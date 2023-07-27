from src.system_analyzer.wrappers.scapy_wrapper import ScapyWrapper
from src.core.log_config import logger


def test_arp_table():
    scapy_wrapper = ScapyWrapper()
    arp_table = scapy_wrapper.get_arp_table("192.168.0.1/24")
    logger.info(f"ARP-TABLE created {arp_table}")

