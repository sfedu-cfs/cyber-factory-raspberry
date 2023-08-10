from pydantic import ValidationError

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_SYSTEM_SERVICES_INFO
from src.schemas.system_services import SingleSystemService, ListSystemService
from src.core.log_config import logger


class SystemServicesCollector:
    """
    Class for collecting system services and their statuses.
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
        """
        lines = self.executor.split('\n')
        services = ListSystemService(items=[])
        for line in lines:
            if line.strip():
                service_info = line.split()
                service = SingleSystemService(name=service_info[0], status=service_info[3])
                services.items.append(service)
        return services.model_dump_json(by_alias=True)


if __name__ == '__main__':
    collector = SystemServicesCollector()
    print(collector.collect_services())


class SystemServices:
    """
    Represents a collection of system services.

    This class collects the system services by executing a shell command and parsing the output.
    It provides methods to collect and print the services and their status.

    Attributes:
        result_command_execute (str): The result of executing the shell command to get the system services.
        services (ListSystemService): A list of system services.

    Example:
        installed_apps = InstalledApplications()
        installed_apps.collect()
        installed_apps.print_applications()
    """

    def __init__(self):
        self.result_command_execute = ""
        self.services = ListSystemService(items=[])

    def collect_services(self):
        """
        Collects the installed services.

        This method parses the output of the shell command execution to extract services names and status.
        It creates instances of the SingleSystemService class for each application and adds them to the
        ListSystemService class.
        """
        try:
            self.result_command_execute = ShellCommandsExecutor(GET_SYSTEM_SERVICES_INFO).execute()
            for line in self.result_command_execute.split("\n"):
                if line.strip():
                    service_info = line.split()
                    print(service_info)
                    service = SingleSystemService(name=service_info[0], status=service_info[3])
                    self.services.items.append(service)
        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting system services: {e}")

    def print_services(self):
        """
        Prints the collected services.

        This method iterates over the services list and prints the name and status of each service.
        """
        for item in self.services.items:
            print(f"Device ID: {item.device_id}")
            print(f"Service Name: {item.name}")
            print(f"Service Status: {item.status}")
            print()


system_services = SystemServices()
system_services.collect_services()
system_services.print_services()
