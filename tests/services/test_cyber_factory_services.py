import pytest

from src.services.cyber_factory_service import CyberFactoryService
from tests.helpers.random_ip import random_ipv4 as random_ip
from tests.helpers.random_mac import get_random_mac_address as random_mac


@pytest.fixture
def obj():
    return CyberFactoryService()


@pytest.fixture
def ip():
    return random_ip()


@pytest.fixture
def ips():
    return random_ip(count=2)


@pytest.fixture
def mac():
    return random_mac()


def test_get_url(obj):
    expected_result = "http://localhost:5000/api/v1/auth/login"
    result = obj._get_url("auth/login")
    assert expected_result == result


def test_login(obj):
    expected_result = True
    result = obj.login()
    assert result == expected_result


def test_send_one_network_interface(obj, ip):
    expected_result = [200, 201]
    # expected_result = None
    result = obj.send_network_interface({"name": "eth11", "ipAddress": ip})
    assert result in expected_result


def test_send_list_network_interface(obj, ips):
    expected_result = [200, 201]
    result = obj.send_list_network_interfaces([{"name": "eth55", "ipAddress": ips[0]},
                                               {"name": "eth51", "ipAddress": ips[1]}])
    assert result in expected_result


def test_send_arp_record(obj, ip, mac):
    response = obj.send_arp_record({"ipAddress": ip, "macAddress": mac})

    assert response["id"] is not None

    assert response["ipAddress"] == ip
    assert response["macAddress"] == mac
