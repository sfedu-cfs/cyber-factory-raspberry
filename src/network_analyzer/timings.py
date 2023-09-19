from src.schemas.count_packet import CountPacket
from src.core.log_config import logger
from src.core.settings import config
from src.helpers.helpers import get_current_time


def init_timings():
    """
    Create a list of CountPacket objects to store the count of internet traffic in certain intervals of time.

    Returns:
        list: A list of CountPacket objects, each representing the count of packets in a certain amount of time.
    """
    try:
        timings = [x.strip() for x in config["NetworkAnalyzer"]["timings"].split(',')]
        count_timings = []
        for timing in timings:
            count = CountPacket(timing=int(timing))
            count.last_update = get_current_time()
            count_timings.append(count)
        return count_timings
    except Exception as e:
        logger.error(f"Error while initializing timings: {e}")
        return


if __name__ == "__main__":
    init_timings()
