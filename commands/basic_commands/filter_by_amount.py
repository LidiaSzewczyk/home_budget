from commands.abs_command import AbsCommand
from commands.by_amount.show_elements_amount import ShowElementsAmount
from commands.by_amount.show_elements_select_amount import ShowElementsSelectAmount
from commands.cli import Cli


class FilterByAmount(AbsCommand):
    name = 'Filter by amount'

    def execute(self):
        commands = (ShowElementsAmount, ShowElementsSelectAmount)

        filter = Cli(commands)
        filter.get_user_command()
