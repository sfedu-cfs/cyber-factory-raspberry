import netifaces
from scapy.all import conf

from .core import ShellCommandsExecutor, GET_NETWORK_INTERFACES_COMMAND


class NetworkInterfaces:
    def __init__(self):
        self.get_network_interfaces_executor = ShellCommandsExecutor(GET_NETWORK_INTERFACES_COMMAND)

    def get_network_interfaces(self):
        list_network_interface = self.get_network_interfaces_executor.execute().split('\n')
        info_about_interfaces = self.parse_list_network_interface(
            list_network_interface
        )
        return info_about_interfaces

    @staticmethod
    def get_primary_network_interface():
        default_gateway = netifaces.gateways()['default'][netifaces.AF_INET]
        for iface in conf.ifaces.values():
            if iface.name == default_gateway[1]:
                return default_gateway[0]
        return None

    @staticmethod
    def parse_list_network_interface(list_network_interface):
        # TODO: обратить внимание на JSON-схемы. Pydantic
        return [
            {
                "name": item.partition(" ")[0], "ipAddress": item.partition(" ")[2]
            }
            for item in list_network_interface
        ]


if __name__ == "__main__":
    ni = NetworkInterfaces()
    networks_interfaces = ni.get_network_interfaces()

    