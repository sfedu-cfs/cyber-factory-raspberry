import pytest

from src.system_analyzer.arp_table import ArpTable


@pytest.fixture
def obj():
    return ArpTable()


def test_get_arp_table(obj):
    print(obj.get_arp_table())
