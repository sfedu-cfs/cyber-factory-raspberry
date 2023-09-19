import requests
import json

from src.core.config import config
from src.core.log_config import logger


class CyberFactoryService:
    def __init__(self):
        self.session = requests.Session()
        self.login()

    def send_system_services(self, services):
        try:
            url = self._get_url("system-services/upload-list")
            response = self.session.post(url, json=services)
            response.raise_for_status()
            logger.info(f"Created system services. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send system services. Error: {e}")

    def send_hosts(self, hosts):
        try:
            url = self._get_url("hosts/upload-list")
            response = self.session.post(url, json=hosts)
            response.raise_for_status()
            logger.info(f"Created hosts. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send hosts. Error: {e}")

    def send_ports(self, ports):
        for port in ports:
            try:
                url = self._get_url("ports/upload-list")
                response = self.session.post(url, json=port.model_dump(by_alias=True))
                response.raise_for_status()
                logger.info(f"Created ports. Status Code: {response.status_code}.")
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to send ports. Error: {e}")

    def send_resources(self, monitoring):
        try:
            url = self._get_url("monitor-resources")
            response = self.session.post(url, json=monitoring)
            response.raise_for_status()
            logger.info(f"Created monitoring. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send monitoring. Error: {e}")

    def send_applications(self, applications):
        try:
            url = self._get_url("applications/upload-list")
            response = self.session.post(url, json=applications)
            response.raise_for_status()
            logger.info(f"Created applications. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send applications. Error: {e}")

    def send_count_packets(self, count_packets):
        try:
            url = self._get_url("count-packets")
            response = self.session.post(url, json=count_packets)
            response.raise_for_status()
            logger.info(f"Created packets. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send packets. Error: {e}.")

    def send_sfc(self, sfc):
        try:
            url = self._get_url("sfc/upload-list")
            response = self.session.post(url, json=sfc)
            response.raise_for_status()
            logger.info(f"Created sfc. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send sfc. Error: {e}")

    def send_arp_table(self, arp_table):
        try:
            url = self._get_url("arp-table/upload-list")
            response = self.session.post(url, json=arp_table)
            response.raise_for_status()
            logger.info(f"Created arp table entries. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send arp table record. Error: {e}")

    def send_network_interfaces(self, network_interfaces):
        try:
            url = self._get_url("network-interfaces/upload-list")
            response = self.session.post(url, data=network_interfaces, headers={"Content-Type": "application/json"})
            response.raise_for_status()
            logger.info(
                f"Created network interface entries. Status Code: {response.status_code}.")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send list of network interface records. Error: {e}")

    def login(self):
        creds = {
            "email": str(config.email),
            "password": str(config.password)
        }
        login_url = self._get_url("auth/login")
        try:
            response = self.session.post(url=login_url, json=creds, timeout=5)
            response.raise_for_status()
            if response.status_code in [200, 201]:
                logger.info("Login successful")
                return True
            else:
                logger.warning(f"Login failed. Invalid credentials. Response: {response.json()}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to login. Error: {e}")
            return False

    @staticmethod
    def _get_url(endpoint):
        return f"{config.base_url}{endpoint}"
