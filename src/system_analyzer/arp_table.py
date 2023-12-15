from pydantic import ValidationError

from src.schemas.arp_table import SingleARP, ListARP
from src.core.log_config import logger


class SystemArpTableCollector:
    """
    Represents a collector for the ARP table from the system files.

    This class reads the ARP table from the '/proc/net/arp' file in Linux systems.
    It parses each line of the file and creates instances of the SingleARP class for each ARP table entry.
    The collected entries are stored in a ListARP object.

    Attributes:
        arp_file_path (str): The path to the system file containing the ARP table.

    Example usage:
        arp_table = SystemArpTableCollector().collect()
        logger.info(arp_table.model_dump_json(by_alias=True, indent=4))
    """

    def __init__(self):
        """
        Initializes an instance of the SystemArpTableCollector class.
        """
        self.arp_file_path = "/proc/net/arp"

    def collect(self):
        """
        Collects the ARP entries from the system file.

        Returns:
            ListARP: A list of SingleARP instances representing the IP and MAC addresses in the ARP table.
        """
        try:
            with open(self.arp_file_path, 'r') as arp_file:
                arp_table = arp_file.readlines()[1:]  # Skip the header line
        except IOError as e:
            logger.error(f"Error opening ARP table file: {e}")
            return None

        arp_entries = ListARP(items=[])

        for line in arp_table:
            try:
                fields = line.split()
                arp_entries.items.append(SingleARP(ip=fields[0], mac=fields[3].upper()))
            except (ValueError, ValidationError) as e:
                logger.error(f"Error parsing ARP table line '{line}': {e}")

        return arp_entries


if __name__ == '__main__':
    at = SystemArpTableCollector().collect()
    logger.info(at.model_dump_json(by_alias=True, indent=4))