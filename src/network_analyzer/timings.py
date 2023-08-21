import os
import configparser

from src.schemas.count_packet import CountPacket
from src.core.log_config import logger

config_path = os.path.join(os.path.dirname(__file__), '../../network_analyzer_settings.ini')
# TODO: add a check for the existence of the file and add default values
# create a parser object
config = configparser.ConfigParser()
# read data from settings.ini
config.read(config_path)


def init_timings():
    """
    Create a list of CountPacket objects to store the count of internet traffic in certain intervals of time.

    Returns:
        list: A list of CountPacket objects, each representing the count of packets in a certain amount of time.
    """
    try:
        if config["traffic"]["timings"] == "":
            logger.error("No timings in settings.ini. Fix it and try again.")
            return
        timings = [x.strip() for x in config["traffic"]["timings"].split(',')]
        count_timings = []
        for timing in timings:
            count = CountPacket(timing=int(timing))
            count_timings.append(count)
        return count_timings
    except Exception as e:
        logger.error(f"Error while initializing timings: {e}")
        return


if __name__ == "__main__":
    init_timings()
