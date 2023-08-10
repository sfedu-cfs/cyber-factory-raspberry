from pydantic import ValidationError

from src.schemas.sfc import SingleSFC
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
        self.result_command_execute = ""
        self.applications = []

    def collect_applications(self):
        """
        Collects the installed applications.

        This method parses the output of the shell command execution to extract application names and versions.
        It creates instances of the SFC class for each application and adds them to the applications list.
        """
        try:
            self.result_command_execute = ShellCommandsExecutor(GET_INSTALLED_APPLICATIONS).execute()
            for line in self.result_command_execute.splitlines():
                name, version = line.strip().split('\t')
                app = SingleSFC(name=name, version=version)
                self.applications.append(app)
        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting applications: {e}")

    def print_applications(self):
        """
        Prints the collected applications.

        This method iterates over the applications list and prints the name and version of each application.
        """
        for app in self.applications:
            print(f"Application Name: {app.name}")
            print(f"Application Version: {app.version}")
            print()


installed_apps = InstalledApplications()
installed_apps.collect_applications()
installed_apps.print_applications()
