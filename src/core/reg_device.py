from src.services.cyber_factory_service import CyberFactoryService
from src.helpers.helpers import get_ip
from src.schemas.reg import RegDevice
from src.core.config import config


def reg_device():
    device = RegDevice()
    device.name = input("Please input device name: ")
    device.cfs_id = int(input("Ask the administrator what your cyber physical system ID is and write it here: "))
    service = CyberFactoryService()
    device.mac = config.mac_address
    device.ip = config.ip_address
    device.net_iface = config.network_interface
    service.register_device(device.model_dump(by_alias=True))


if __name__ == "__main__":
    reg_device()
