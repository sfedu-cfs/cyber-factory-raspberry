import subprocess


class ShellCommandsExecutor:
    def __init__(self, command):
        self.command = command

    def execute(self, *args):
        # TODO: check shell = True for best practice
        command = self.__format_command(self.command, args)
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            encoding='utf-8',
        )
        return result.stdout.strip()

    def __format_command(self, command, command_args):
        if not command_args:
            return command
        return command.format(*command_args)