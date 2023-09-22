from src.services.cyber_factory_service import CyberFactoryService
from src.helpers.helpers import get_mac, get_ip, get_ip_iface
from src.schemas.reg import RegDevice


def reg_device():
    device = RegDevice()
    device.name = input("Please input device name: ")
    device.cfs_id = int(input("Ask the administrator what your cyber physical system ID is and write it here: "))
    service = CyberFactoryService()
    device.mac = get_mac()
    device.ip = get_ip()
    device.net_iface = get_ip_iface(device.ip)
    service.register_device(device.model_dump(by_alias=True))


if __name__ == "__main__":
    reg_device()
