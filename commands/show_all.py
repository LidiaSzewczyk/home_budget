from commands.abs_command import AbsCommand


class ShowAll(AbsCommand):
    name = 'Show all'

    def execute(self):
        for amount in self.dashboard:
            print(amount)