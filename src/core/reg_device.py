from src.services.cyber_factory_service import CyberFactoryService
from src.helpers.helpers import get_mac, get_ip, get_ip_iface


def reg_device():
    name = input("Please input device name: ")
    cfs_id = input("Ask the administrator what your cyber physical system ID is and write it here: ")
    service = CyberFactoryService()
    mac = get_mac()
    ip = get_ip()
    iface = get_ip_iface(ip)
    service.register_device(name=name, mac=mac, ip=ip, network_interface=iface, cfs=cfs_id)


if __name__ == "__main__":
    reg_device()
