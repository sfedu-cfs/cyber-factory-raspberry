import pytest

from src.services.cyber_factory_service import CyberFactoryService


@pytest.fixture
def obj():
    return CyberFactoryService()


def test_get_url(obj):
    expected_result = "http://localhost:5000/api/v1/auth/login"
    result = obj._get_url("auth/login")
    assert expected_result == result


def test_login(obj):
    expected_result = True
    result = obj.login()
    assert result == expected_result


def test_send_one_network_interface(obj):
    expected_result = [200, 201]
    # expected_result = None
    result = obj.send_network_interface({"name": "eth11", "ipAddress": "192.168.1.102"})
    assert result in expected_result


def test_send_list_network_interface(obj):
    expected_result = [200, 201]
    # expected_result = None
    result = obj.send_list_network_interfaces([{"name": "eth55", "ipAddress": "192.168.1.100"},
                                              {"name": "eth51", "ipAddress": "192.168.1.102"}])
    assert result in expected_result
