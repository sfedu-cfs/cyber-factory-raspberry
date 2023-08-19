from pydantic import ValidationError

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_SYSTEM_SERVICES_INFO
from src.schemas.system_services import SingleSystemService, ListSystemService
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
        self.executor = ShellCommandsExecutor(GET_SYSTEM_SERVICES_INFO)

    def collect(self):
        """
        Collects system services and their statuses.

        Returns:
            ListSystemService: A ListSystemService object containing the collected system services.
        """
        try:
            output = self.executor.execute()
            lines = output.split('\n')[1:-6]
            services = ListSystemService(items=[])
            for line in lines:
                if line.strip():
                    service_info = line.split()
                    service = SingleSystemService(name=service_info[0], status=service_info[3])
                    services.items.append(service)

        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting system services: {e}")
            raise e

        return services
