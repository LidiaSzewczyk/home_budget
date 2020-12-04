from commands.null_command import NoCommand


class Cli:
    def __init__(self, commands):
        self.commands = commands
        self._user_idx = ''

    @property
    def user_idx(self):
        return self._user_idx

    @user_idx.setter
    def user_idx(self):
        self._user_idx = input("Provide id.\n")

    def run(self):
        while True:
            self.get_user_command()

    def get_user_command(self):
        for idx, command in enumerate([command for key, command in self.get_commands().items() if key.isdigit()]):
            print(f'{idx + 1}. {command.name}')
        user_command = input("Choose command.\n")
        command = self.parse_command(user_command)
        command.execute()

    def get_commands(self):
        command_name = {cls.name: cls for cls in self.commands}
        command_idx = {str(idx + 1): cls for idx, cls in enumerate(self.commands)}
        command_name.update(command_idx)
        return command_name

    def parse_command(self, user_command):
        commands = self.get_commands()
        command = commands.setdefault(user_command, NoCommand)
        return command(user_command)


#  TODO not work !!!