from src.schemas.ports import ListPort, SinglePort
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import SCAN_PORTS
from src.system_analyzer.hosts import HostCollector


class PortCollector:
    def __init__(self):
        self.hosts = HostCollector().collect()

    def collect(self):
        ports = ListPort(items=[])
        for host in self.hosts.items:
            ports_result_command_execute = ShellCommandsExecutor(f"{SCAN_PORTS} {host.ip}").execute()
            for line in ports_result_command_execute.strip().splitlines():
                if "Starting" not in line and "/" in line:
                    port_number, status, service = line.split()[:4]
                    port_number, protocol = port_number.split('/')
                    single_port = SinglePort(ip=host.ip, port=int(port_number), status=status, service=service,
                                             protocol=protocol)
                    ports.items.append(single_port)

        return ports


if __name__ == "__main__":
    pc = PortCollector().collect()
    print(pc.model_dump_json(by_alias=True, indent=4))
