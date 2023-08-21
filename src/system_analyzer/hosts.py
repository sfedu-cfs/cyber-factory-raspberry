from src.system_analyzer.core.commands import SCAN_HOSTS
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.network_interfaces import DEFAULT_GATEWAY_IP
from src.schemas.hosts import BaseHost, ListHost
from src.helpers.helpers import get_mac


class HostCollector:
    def __init__(self):
        """
        Initializes the HostsCollector object.
        """
        self.hosts_result_command_execute = ShellCommandsExecutor(f"{SCAN_HOSTS} {DEFAULT_GATEWAY_IP}").execute()

    def collect(self):
        """
        Collects the hosts information.

        Returns:
            ListHost: A ListHost object containing the collected hosts information.
        """
        hosts = ListHost(items=[])
        lines = self.hosts_result_command_execute.strip().splitlines()
        for i in range(len(lines)):
            if "Nmap scan report" in lines[i]:
                ip = lines[i].split()[-1]
                mac_address = get_mac()
                try:
                    if "MAC Address" in lines[i + 2]:
                        mac_address = lines[i + 2].split()[2]
                except IndexError:
                    pass
                single_host = BaseHost(ip=ip, mac=mac_address)
                hosts.items.append(single_host)

        return hosts


if __name__ == "__main__":
    hc = HostCollector().collect()
    print(hc.model_dump_json(by_alias=True, indent=4))