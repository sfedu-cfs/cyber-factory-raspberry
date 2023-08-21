import requests

from src.core.config import config
from src.core.log_config import logger
from src.helpers.helpers import device_id


class CyberFactoryService:
    MAX_RETRIES = 10

    def __init__(self):
        # TODO: Почитать про сессию, использование контекстного менеджера requests
        self.session = requests.Session()
        self.login()

    @classmethod
    def send_sfc(cls, sfc):
        try:
            url = cls._get_url("sfc")
            response = requests.post(url, json=sfc.model_dump(by_alias=True))
            response.raise_for_status()
            logger.info(f"Code: {response.status_code} Created sfc {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(e)

    @classmethod
    def send_arp_record(cls, arp_table):
        data = cls._construct_data(arp_table)
        try:
            response = requests.post(cls._get_url("arp-table"), json=data)
            response.raise_for_status()
            logger.info(f"Code: {response.status_code} Created arp table entry {response.json()}")
            # return response.status_code
            return response.json()
        except requests.exceptions.RequestException as e:
            # TODO: Написать логгинг в какой функции ошибка
            logger.error(e)

    @classmethod
    def send_list_arp_records(cls, list_arp):
        data = cls._construct_data(list_arp)
        try:
            response = requests.post(cls._get_url("arp-table/upload-list"), json=data)
            response.raise_for_status()
            # TODO: Тут не приходит JSON в ответ, надо чтобы приходил
            logger.info(f"Created arp table entries")
            return response.status_code
        except requests.exceptions.RequestException as e:
            logger.error(e)

    @classmethod
    def send_network_interface(cls, network_interface):
        data = cls._construct_data(network_interface)
        try:
            response = requests.post(cls._get_url("network-interfaces"), json=data)
            response.raise_for_status()
            logger.info(f"Code: {response.status_code} Created network interface entry {response.json()}")
            return response.status_code
        except requests.exceptions.RequestException as e:
            # TODO: Написать логгинг в какой функции ошибка
            logger.error(e)

    @classmethod
    def send_list_network_interfaces(cls, list_network_interfaces):
        data = cls._construct_data(list_network_interfaces)
        try:
            response = requests.post(cls._get_url("network-interfaces/upload-list"), json=data)
            response.raise_for_status()
            # TODO: Тут не приходит JSON в ответ, надо чтобы приходил
            logger.info(f"Created network interfaces entries")
            return response.status_code
        except requests.exceptions.RequestException as e:
            logger.error(e)

    @classmethod
    def login(cls):
        # TODO: Попробовать вынести MAX_RETRIES за пределы функции логин
        creds = {
            "email": str(config.email),
            "password": str(config.password)
        }
        login_url = cls._get_url("auth/login")
        retries = 0
        while retries <= cls.MAX_RETRIES:
            try:
                response = requests.post(url=login_url, json=creds, timeout=5)
                response.raise_for_status()
                if response.status_code in [200, 201]:
                    logger.info(f"Login successful")
                    return True
                else:
                    logger.warning(f"Login failed. Invalid credentials. {response.json()}")
                    return False
            except requests.exceptions.RequestException as e:
                logger.error(e)
                retries += 1
        logger.error("Max retries exceeded. Login failed.")
        return False

    @staticmethod
    def _construct_data(data):
        if isinstance(data, dict):
            return {
                "deviceMacAddress": device_id,
                **data
            }
        else:
            return {
                "deviceMacAddress": device_id,
                "items": data
            }

    @staticmethod
    def _get_url(endpoint):
        return f"{config.base_url}{endpoint}"
