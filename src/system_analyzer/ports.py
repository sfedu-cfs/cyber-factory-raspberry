from src.schemas.ports import ListPort, BasePort
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import SCAN_PORTS
from src.system_analyzer.hosts import HostCollector


class PortCollector:
    def __init__(self):
        self.hosts = HostCollector().collect()

    def collect(self):
        # TODO: remake it for new api
        ports = []
        for host in self.hosts.items:
            port = ListPort(ip=host.ip, items=[])
            ports_result_command_execute = ShellCommandsExecutor(f"{SCAN_PORTS} {host.ip}").execute()
            for line in ports_result_command_execute.strip().splitlines():
                if "Starting" not in line and "/" in line:
                    port_number, status, service = line.split()[:4]
                    port_number, protocol = port_number.split('/')
                    if status != "filtered":
                        single_port = BasePort(port=int(port_number), status=status, service=service,
                                               protocol=protocol)
                        port.items.append(single_port)
            ports.append(port)

        return ports


if __name__ == "__main__":
    pc = PortCollector().collect()
    for port in pc:
        print(port.model_dump_json(by_alias=True))
