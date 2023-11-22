# TODO: Write a test
import pytest
from unittest.mock import MagicMock

from datetime import time, timedelta
from src.network_analyzer.handlers.packet_handler import send_to_server


class MockOutput:
    def __init__(self, timing, last_update):
        self.timing = timing
        self.last_update = last_update

    def model_dump(self, by_alias=True):
        return "model_dump"


@pytest.fixture
def mock_service():
    return MagicMock()


@pytest.mark.parametrize(
    "timing, last_update, diff_seconds, expected_send_count_packets",
    [
        (10, time(hour=0, minute=0, second=0), 5, True),
        (10, time(hour=0, minute=0, second=0), 15, True),
        (10, time(hour=0, minute=0, second=0), -5, True),
        (10, time(hour=0, minute=0, second=0), -15, False),
    ],
)
def test_send_to_server(mock_service, timing, last_update, diff_seconds, expected_send_count_packets):
    output = MockOutput(timing, last_update)
    # current_time = last_update + timedelta(seconds=diff_seconds)
    current_time = time(hour=0, minute=0, second=diff_seconds)
    send_to_server(output)

    if expected_send_count_packets:
        mock_service.send_count_packets.assert_called_once_with("model_dump")
    else:
        mock_service.send_count_packets.assert_not_called()
