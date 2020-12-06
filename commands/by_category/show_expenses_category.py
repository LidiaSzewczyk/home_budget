from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class ShowExpensesCategory(AbsCommand):
    name = 'Show expenses by category'

    def execute(self):

        db = DbConnection().db
        c = db.cursor()

        c.execute('SELECT * FROM expenses ORDER BY category')
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')



