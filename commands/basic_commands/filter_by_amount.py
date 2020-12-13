from commands.abs_command import AbsCommand
from commands.by_amount.show_expenses_amount import ShowExpensesAmount
from commands.by_amount.show_expenses_select_amount import ShowExpensesSelectAmount
from commands.cli import Cli



class FilterByAmount(AbsCommand):
    name = 'Filter by amount'

    def execute(self):
        commands = (ShowExpensesAmount, ShowExpensesSelectAmount)

        filter = Cli(commands)
        filter.get_user_command()
