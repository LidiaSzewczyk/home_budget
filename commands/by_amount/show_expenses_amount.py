from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class ShowExpensesAmount(AbsCommand):
    name = 'Show expenses by amount'

    def execute(self):

        db = DbConnection().db
        c = db.cursor()

        c.execute('SELECT * FROM expenses ORDER BY amount DESC')
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')



