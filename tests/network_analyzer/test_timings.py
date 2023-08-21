import pytest

from src.network_analyzer.timings import init_timings, config
from src.schemas.count_packet import CountPacket

# Get timings from the config file and convert them to a list of integers
timing_values = list(map(int, config["traffic"]["timings"].split(',')))


@pytest.mark.parametrize("expected_result", [[
    CountPacket(timing=value) for value in timing_values
]])
def test_init_timings(expected_result):
    timings = init_timings()
    assert timings == expected_result
