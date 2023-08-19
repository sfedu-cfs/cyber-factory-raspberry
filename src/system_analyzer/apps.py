from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.system_analyzer.core.commands import GET_INFO_ABOUT_APPLICATIONS
from src.schemas.apps import SingleApp, ListApp


class AppsCollector:
    def __init__(self):
        self.result_command_execute = ShellCommandsExecutor(GET_INFO_ABOUT_APPLICATIONS).execute()

    def collect(self):
        apps = []
        for line in self.result_command_execute.splitlines():
            app_info = line.split('\t')
            if len(app_info) == 3:
                name, version, description = app_info
                app = SingleApp(name=name, version=version, description=description)
                apps.append(app)

        return ListApp(items=apps)


ap = AppsCollector().collect()
print(ap.model_dump_json(by_alias=True))
