import netifaces
from scapy.all import conf

from src.system_analyzer.core import (
    ShellCommandsExecutor, GET_NETWORK_INTERFACES_IPS_COMMAND, GET_NETWORK_INTERFACES_NAMES_COMMAND
)


class NetworkInterfaces:
    def __init__(self):
        self.network_interfaces_ips = ShellCommandsExecutor(GET_NETWORK_INTERFACES_IPS_COMMAND)
        self.network_interfaces_names = ShellCommandsExecutor(GET_NETWORK_INTERFACES_NAMES_COMMAND)

    def get_list_network_interfaces(self):
        list_network_interface_with_ips = self.network_interfaces_ips.execute().split('\n')
        parsed_network_interfaces_ips = self.parse_network_interfaces_ips(list_network_interface_with_ips)
        list_network_interface_names = self.network_interfaces_names.execute().split('\n')
        missing_interfaces = []
        for name in list_network_interface_names:
            if name not in [interface["name"] for interface in parsed_network_interfaces_ips]:
                missing_interfaces.append({"name": name, "ipAddress": None})
        parsed_network_interfaces_ips.extend(missing_interfaces)
        return parsed_network_interfaces_ips

    def get_primary_network_interface_with_mask(self):
        list_network_interface_with_mask = self.get_list_network_interfaces()

        default_gateway = netifaces.gateways()['default'][netifaces.AF_INET]
        for iface in conf.ifaces.values():
            if iface.name == default_gateway[1]:
                return default_gateway[0]
        return None

    @staticmethod
    def parse_network_interfaces_ips(list_network_interfaces_ips):
        # TODO: обратить внимание на JSON-схемы. Pydantic
        return [
            {
                "name": item.partition(" ")[0], "ipAddress": item.partition(" ")[2]
            }
            for item in list_network_interfaces_ips
        ]

    @staticmethod
    def get_network_interfaces_mask(list_network_interfaces):
        return [
            {
                "name": item["name"], "netmask": item["ipAddress"].split('/')[1] if item["ipAddress"] else None
            }
            for item in list_network_interfaces
        ]
