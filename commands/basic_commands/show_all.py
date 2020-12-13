from commands.abs_command import AbsCommand
from commands.basic_commands.show_expenses import ShowExpenses
from commands.basic_commands.show_income import ShowIncome


class ShowAll(AbsCommand):
    name = 'Show all'

    def execute(self):

        expenses = ShowExpenses()
        income = ShowIncome()
        expenses.execute()
        income.execute()

