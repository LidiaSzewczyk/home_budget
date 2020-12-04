from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from commands.show_expenses import ShowExpenses
from commands.show_income import ShowIncome
from dbs.DbConnection import DbConnection


class ShowAll(AbsCommand):
    name = 'Show all'

    def execute(self):

        expenses = ShowExpenses()
        income = ShowIncome()
        expenses.execute()
        income.execute()

        # db = DbConnection().db
        # c = db.cursor()
        #
        # c.execute('SELECT * FROM expenses')
        # expenses = c.fetchall()
        #
        # for amount in expenses:
        #     print(Expense(amount))
        #
        # c.execute('SELECT * FROM income')
        # income = c.fetchall()
        # for amount in income:
        #     print(Income(amount))

