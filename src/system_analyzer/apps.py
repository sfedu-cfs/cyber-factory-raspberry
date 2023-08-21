from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_INFO_ABOUT_APPLICATIONS
from src.schemas.apps import BaseSingleApp, ListApp


class AppsCollector:
    def __init__(self):
        """
        Initializes an instance of the AppsCollector class.

        This constructor executes a shell command to get information about applications installed on the system.
        The result of the command execution is stored in the `result_command_execute` attribute.
        """
        self.result_command_execute = ShellCommandsExecutor(GET_INFO_ABOUT_APPLICATIONS).execute()

    def collect(self):
        """
        Collects information about applications installed on the system.

        This method parses the output of the shell command execution and creates instances of the SingleApp model
        for each application found. The SingleApp instances are then added to a ListApp model.

        Returns:
            ListApp: An instance of the ListApp model containing information about the installed applications.
        """
        apps = []
        for line in self.result_command_execute.splitlines():
            app_info = line.split('\t')
            # TODO: fix this
            if len(app_info) == 3:
                name, version, description = app_info
                app = BaseSingleApp(name=name, version=version, description=description)
                apps.append(app)

        return ListApp(items=apps)


if __name__ == '__main__':
    ap = AppsCollector().collect()
    print(ap.model_dump_json(by_alias=True, indent=4))
