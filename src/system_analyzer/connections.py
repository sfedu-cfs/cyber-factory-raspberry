from pydantic import ValidationError
from ipaddress import IPv6Address, AddressValueError

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_CONNECTIONS
from src.schemas.connections import BaseSingleConnection, ListConnection
from src.core.log_config import logger


class ConnectionsCollector:
    def __init__(self):
        """
        Initializes an instance of the ConnectionsCollector class.

        This constructor executes a shell command to get information about connections on the system.
        The result of the command execution is stored in the `result_command_execute` attribute.
        """
        self.result_command_execute = ShellCommandsExecutor(GET_CONNECTIONS).execute()

    @staticmethod
    def ipv6_expand(ip_address):
        """
        Expands an IPv6 address.

        Args:
            ip_address (str): The IPv6 address to expand.

        Returns:
            str: The expanded IPv6 address.
        """
        ip, sep, port = ip_address.rpartition(':')
        try:
            return IPv6Address(ip).exploded, port
        except AddressValueError:
            # Если адрес не является IPv6, вернуть его без изменений
            return ip, port

    def collect(self):
        """
        Collects information about connections on the system.

        This method parses the output of the shell command execution and creates instances of the SingleConnection model
        for each connection found. The SingleConnection instances are then added to a ListConnection model.

        Returns:
            ListConnection: An instance of the ListConnection model containing information about the connections.
        """
        try:
            connections = ListConnection(items=[])
            lines = self.result_command_execute.splitlines()[2:]
            for line in lines:
                connection_info = line.split()
                if len(connection_info) == 7:
                    protocol, recv_q, send_q, local, foreign, state, service_name = connection_info
                    if protocol == "tcp6" or protocol == "udp6":
                        src_ip_address, src_port = self.ipv6_expand(local.strip())
                        dst_ip_address, dst_port = self.ipv6_expand(foreign.strip())
                    else:
                        src_ip_address, src_port = local.strip().split(':')
                        dst_ip_address, dst_port = foreign.strip().split(':')
                    if dst_port == "*":
                        dst_port = 0
                    connection = BaseSingleConnection(protocol=protocol, src_ip_address=src_ip_address,
                                                      src_port=src_port,
                                                      dst_ip_address=dst_ip_address, dst_port=dst_port, state=state,
                                                      service_name=service_name)
                    connections.items.append(connection)

        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting connections: {e}")
            raise e
        return connections


if __name__ == '__main__':
    ap = ConnectionsCollector().collect()
    print(ap.model_dump_json(by_alias=True, indent=4))
