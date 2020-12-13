from amount.expense import Expense
from commands.abs_command import AbsCommand
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowExpenses(AbsCommand):
    name = 'Show all expenses'

    def execute(self):
        query = 'SELECT * FROM expenses ORDER BY created DESC'
        expenses = DbSelectAll().do(query)

        for amount in expenses:
            print(Expense(amount))
