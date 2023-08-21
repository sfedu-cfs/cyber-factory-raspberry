import netifaces

from scapy.all import conf

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_NETWORK_INTERFACES_IPS, GET_NETWORK_INTERFACES_NAMES
from src.schemas.interfaces import BaseSingleNetworkInterface, ListNetworkInterface, BaseSingleNetworkInterfaceMask


class NetworkInterfaces:
    def __init__(self):
        self.network_interfaces_ips = ShellCommandsExecutor(GET_NETWORK_INTERFACES_IPS).execute().split('\n')
        self.network_interfaces_names = ShellCommandsExecutor(GET_NETWORK_INTERFACES_NAMES).execute().split('\n')

    def get_list_network_interfaces(self):
        parsed_network_interfaces_ips = self.parse_network_interfaces_data(self.network_interfaces_ips)
        missing_interfaces = ListNetworkInterface(items=[])
        for name in self.network_interfaces_names:
            if name not in [interface.name for interface in parsed_network_interfaces_ips.items]:
                missing_interfaces.items.append(BaseSingleNetworkInterface(name=name))
        parsed_network_interfaces_ips.items.extend(missing_interfaces.items)
        return parsed_network_interfaces_ips

    def get_primary_network_interface_with_mask(self):
        network_interfaces_mask = self.get_network_interfaces_mask()
        default_gateway = netifaces.gateways()['default'][netifaces.AF_INET]
        for iface in conf.ifaces.values():
            if iface.name == default_gateway[1]:
                primary_interface = next(
                    (iface for iface in network_interfaces_mask if iface.name == default_gateway[1]), None)
                if primary_interface:
                    return f"{default_gateway[0]}/{primary_interface.netmask}"
        return None

    def get_network_interfaces_mask(self):
        return [
            BaseSingleNetworkInterfaceMask(name=iface.name,
                                           netmask=iface.ip.split('/')[1] if iface.ip else None)
            for iface in self.get_list_network_interfaces().items
        ]

    @staticmethod
    def parse_network_interfaces_data(list_network_interfaces):
        return ListNetworkInterface(items=[
            BaseSingleNetworkInterface(name=item.partition(" ")[0], ip=item.partition(" ")[2])
            for item in list_network_interfaces
        ])


ni = NetworkInterfaces()
DEFAULT_GATEWAY_IP = ni.get_primary_network_interface_with_mask()
if __name__ == "__main__":
    print(ni.get_list_network_interfaces().model_dump_json(by_alias=True, indent=4))
    for interface in ni.get_network_interfaces_mask():
        print(interface.model_dump_json(by_alias=True, indent=4))
    print(ni.get_primary_network_interface_with_mask())
