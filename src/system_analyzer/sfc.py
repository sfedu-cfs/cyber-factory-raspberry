from pydantic import ValidationError

from src.schemas.sfc import BaseSingleSFC, ListSFC
from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_INSTALLED_APPLICATIONS
from src.core.log_config import logger


class SFCCollector:
    """
    Represents a collector for SFCs.

    This class uses a ShellCommandsExecutor instance to execute a shell command and retrieve names and versions of
    installed applications.
    It parses the output of the command and creates instances of the SingleSFC class for each app.
    The collected SFCs are stored in a ListSFC object.

    Attributes:
        result_command_execute (str): The result of executing the shell command to get the installed applications.

    Example usage:
        sfc = SFCCollector().collect()
        print(sfc.model_dump_json(by_alias=True)
    """

    def __init__(self):
        """
        Initializes the SFCCollector with a ShellCommandsExecutor instance.
        """
        self.result_command_execute = ShellCommandsExecutor(GET_INSTALLED_APPLICATIONS).execute()

    def collect(self):
        """
        Collects the SFCs.

        This method parses the output of the shell command execution to extract application names and versions.
        It creates instances of the SingleSFC class for each application and adds them to the SFC list.

        Returns:
            ListSFC: A list of SingleSFC instances representing the name and version of installed applications.
        """
        try:
            sfcs = ListSFC(items=[])
            for line in self.result_command_execute.splitlines():
                name, version = line.strip().split('\t')
                app = BaseSingleSFC(name=name, version=version)
                sfcs.items.append(app)
        except (ValidationError, Exception) as e:
            logger.error(f"Error collecting applications: {e}")
            raise e

        return sfcs


if __name__ == "__main__":
    sfc = SFCCollector().collect()
    print(sfc.model_dump(by_alias=True))
