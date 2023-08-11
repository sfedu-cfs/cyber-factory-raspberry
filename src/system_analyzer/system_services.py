from pydantic import ValidationError

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_SYSTEM_SERVICES_INFO
from src.schemas.system_services import SingleSystemService, ListSystemService
from src.core.log_config import logger


class SystemServicesCollector:
    """
    Collects system services and their statuses.

    This class uses a ShellCommandsExecutor instance to execute a shell command and retrieve the system services.
    It parses the output of the command and creates instances of the SingleSystemService class for each service.
    The collected services are stored in a ListSystemService object.

    Attributes:
        executor (ShellCommandsExecutor): An instance of ShellCommandsExecutor used to execute the shell command.

    Example:
        collector = SystemServicesCollector()
        services = collector.collect_services()
    """

    def __init__(self):
        self.executor = ShellCommandsExecutor(GET_SYSTEM_SERVICES_INFO).execute()
        """
        Initializes the SystemServicesCollector with a ShellCommandsExecutor instance.
        """

    def collect_services(self):
        """
        Collects system services and their statuses.

        Returns:
            ListSystemService: A ListSystemService object containing the collected system services.
            None: If an error occurs during collection.
        """
        try:
            lines = self.executor.split('\n')[1:-6]
            services = ListSystemService(items=[])
            for line in lines:
                if line.strip():
                    service_info = line.split()
                    service = SingleSystemService(name=service_info[0], status=service_info[3])
                    services.items.append(service)

        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting system services: {e}")
            raise e

        return services.model_dump_json(by_alias=True)


system_services = SystemServicesCollector().collect_services()
print(system_services)

