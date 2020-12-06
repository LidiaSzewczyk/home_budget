from commands.abs_command import AbsCommand
from commands.by_category.show_expenses_category import ShowExpensesCategory
from commands.by_category.show_expenses_select_category import ShowExpensesSelectCategory
from commands.by_category.show_sum_expenses_category import ShowSumExpensesCategory
from commands.cli import Cli



class FilterByCategory(AbsCommand):
    name = 'Filter by category'

    def execute(self):
        commands = (ShowExpensesCategory, ShowExpensesSelectCategory, ShowSumExpensesCategory)

        filter = Cli(commands)
        filter.get_user_command()
