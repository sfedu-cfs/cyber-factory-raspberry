from pydantic import ValidationError

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_SYSTEM_SERVICES_INFO
from src.schemas.system_services import ListSystemService, BaseSingleSystemService
from src.core.log_config import logger


class SystemServicesCollector:
    """
    Represents a collector for system services.

    This class uses a ShellCommandsExecutor instance to execute a shell command and retrieve names and status of
    system services.
    It parses the output of the command and creates instances of the SingleSystemService class for each service.
    The collected services are stored in a ListSystemService object.

    Attributes:
        executor (ShellCommandsExecutor): An instance of ShellCommandsExecutor used to execute the shell command.

    Example usage:
        sys_services = SFCCollector().collect()
        print(sys_services.model_dump_json(by_alias=True)
    """

    def __init__(self):
        """
        Initializes the SystemServiceCollector with a ShellCommandsExecutor instance.
        """
        self.executor = ShellCommandsExecutor(GET_SYSTEM_SERVICES_INFO).execute()

    def collect(self):
        """
        Collects system services and their statuses.

        Returns:
            ListSystemService: A ListSystemService object containing the collected system services.
        """
        try:
            # [1:-6] - remove the first and the last 6 lines of the output of the command with support info
            lines = self.executor.split('\n')[1:-6]
            services = ListSystemService(items=[])
            for line in lines:
                if line.strip():
                    service_info = line.split()
                    service = BaseSingleSystemService(name=service_info[0], status=service_info[3])
                    services.items.append(service)

        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting system services: {e}")
            raise e

        return services


if __name__ == "__main__":
    ss = SystemServicesCollector().collect()
    print(ss.model_dump_json(by_alias=True, indent=4))
