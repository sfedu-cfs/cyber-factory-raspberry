import pytest
import requests

from unittest.mock import MagicMock, patch

from src.core.config import config
from src.services.cyber_factory_service import CyberFactoryService
from src.schemas.sfc import ListSFC, BaseSingleSFC
from src.schemas.arp_table import ListARP, BaseSingleARP
from src.schemas.interfaces import ListNetworkInterface, BaseSingleNetworkInterface
from src.schemas.system_services import ListSystemService, BaseSingleSystemService
from src.schemas.hosts import ListHost, BaseHost
from src.schemas.ports import ListPort, BasePort
from src.schemas.monitor_resources import MonitorResource
from src.schemas.apps import ListApp, BaseSingleApp
from src.schemas.count_packet import CountPacket
from src.helpers.helpers import get_mac


@pytest.fixture
def cyber_factory_service():
    return CyberFactoryService()


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_sfc_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "SFC created successfully"}
    mock_post.return_value = mock_response

    sfc_data = ListSFC(items=[BaseSingleSFC(name="SFC 1", version="1.0.0"),
                              BaseSingleSFC(name="SFC 2", version="1.0.0")])
    response = cyber_factory_service.send_sfc(sfc_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}sfc/upload-list",
        json=sfc_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "SFC created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_sfc_failure(mock_post, cyber_factory_service):
    mock_post.side_effect = requests.exceptions.RequestException("Failed to send request")

    sfc_data = ListSFC(items=[BaseSingleSFC(name="SFC 1", version="1.0.0"),
                              BaseSingleSFC(name="SFC 2", version="1.0.0")])
    response = cyber_factory_service.send_sfc(sfc_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}sfc/upload-list",
        json=sfc_data.model_dump(by_alias=True),
    )
    assert response is None


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_arp_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "ARP entries created successfully"}
    mock_post.return_value = mock_response

    arp_data = ListARP(items=[BaseSingleARP(ip="1.1.1.1", mac=get_mac()),
                              BaseSingleARP(ip="2.2.2.2", mac=get_mac())])
    response = cyber_factory_service.send_arp_table(arp_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}arp-table/upload-list",
        json=arp_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "ARP entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_netifaces_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Network Interfaces entries created successfully"}
    mock_post.return_value = mock_response

    ni_data = ListNetworkInterface(items=[BaseSingleNetworkInterface(name="eth0", ip="1.1.1.1/24"),
                                          BaseSingleNetworkInterface(name="eth1", ip="2.2.2.2/24")])
    response = cyber_factory_service.send_network_interfaces(ni_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}network-interfaces/upload-list",
        json=ni_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Network Interfaces entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_system_services_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "System Services entries created successfully"}
    mock_post.return_value = mock_response

    ss_data = ListSystemService(items=[BaseSingleSystemService(name="ss1", status="active"),
                                       BaseSingleSystemService(name="ss2", status="exited")])

    response = cyber_factory_service.send_system_services(ss_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}system-services/upload-list",
        json=ss_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "System Services entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_hosts_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Hosts entries created successfully"}
    mock_post.return_value = mock_response

    hosts_data = ListHost(items=[BaseHost(ip="1.1.1.1", mac="00:00:00:00:00:00"),
                                 BaseHost(ip="2.2.2.2", mac="01:00:00:00:00:00")])

    response = cyber_factory_service.send_hosts(hosts_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}hosts/upload-list",
        json=hosts_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hosts entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_ports_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Ports entries created successfully"}
    mock_post.return_value = mock_response

    ports_data = ListPort(items=[BasePort(port="8080", protocol="tcp"),
                                 BasePort(port="8081", protocol="udp")])

    response = cyber_factory_service.send_ports(ports_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}ports/upload-list",
        json=ports_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Ports entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_monitoring_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Monitoring entries created successfully"}
    mock_post.return_value = mock_response

    # TODO: Add data
    monitoring_data = MonitorResource()

    response = cyber_factory_service.send_resources(monitoring_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}monitor-resources",
        json=monitoring_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Monitoring entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_applications_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Applications entries created successfully"}
    mock_post.return_value = mock_response

    apps_data = ListApp(items=[BaseSingleApp(name="app1", version="1.0.0", description="App 1"),
                               BaseSingleApp(name="app2", version="1.0.0", description="App 2")])

    response = cyber_factory_service.send_applications(apps_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}applications/upload-list",
        json=apps_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Applications entries created successfully"}


@patch("src.services.cyber_factory_service.requests.Session.post")
def test_send_count_packets_success(mock_post, cyber_factory_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Count Packets entries created successfully"}
    mock_post.return_value = mock_response

    # TODO: Add data
    count_packets_data = CountPacket(timing=5)

    response = cyber_factory_service.send_count_packets(count_packets_data.model_dump(by_alias=True))

    mock_post.assert_called_once_with(
        f"{config.base_url}count-packets",
        json=count_packets_data.model_dump(by_alias=True),
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Count Packets entries created successfully"}