import json

from pydantic import ValidationError

from src.schemas.sfc import SFC
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_INSTALLED_APPLICATIONS
from src.core.log_config import logger


class InstalledApplications:
    """
    Represents a collection of installed applications.

    This class collects the installed applications by executing a shell command and parsing the output.
    It provides methods to collect and print the applications.

    Attributes:
        result_command_execute (str): The result of executing the shell command to get the installed applications.
        applications (list[SFC]): A list of SFC instances representing the installed applications.

    Example:
        installed_apps = InstalledApplications()
        installed_apps.collect()
        installed_apps.print_applications()
    """

    def __init__(self):
        self.result_command_execute = ShellCommandsExecutor(GET_INSTALLED_APPLICATIONS).execute()
        self.applications = []

    def collect(self):
        """
        Collects the installed applications.

        This method parses the output of the shell command execution to extract application names and versions.
        It creates instances of the SFC class for each application and adds them to the applications list.
        """
        for line in self.result_command_execute.splitlines():
            try:
                name, version = line.strip().split('\t')
                app = SFC(name=name, version=version)
                self.applications.append(app)
            except ValidationError as e:
                logger.error(e)

    def print_applications(self):
        """
        Prints the collected applications.

        This method iterates over the applications list and prints the name and version of each application.
        """
        for app in self.applications:
            print(f"Application Name: {app.name}")
            print(f"Application Version: {app.version}")
            print(f"Device ID: {app.device_id}")
            print()


installed_apps = InstalledApplications()
installed_apps.collect()
installed_apps.print_applications()

