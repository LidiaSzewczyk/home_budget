from commands.abs_command import AbsCommand


class NoCommand(AbsCommand):
    name = "No command"

    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'No command: {self.name}')
