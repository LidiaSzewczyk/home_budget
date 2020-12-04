from commands.abs_command import AbsCommand

from dbs.DbConnection import DbConnection
from amount.expense import Expense


class ShowExpensesSelectAmount(AbsCommand):
    name = 'Show expenses - select amounts'
    Expense = Expense

    def __init__(self):
        self.min_amount = input('Provide min amount\n')
        self.max_amount = input('Provide max amount\n')

        if self.min_amount == '':
            self.min_amount = 0

        else:
            self.min_amount = float(self.min_amount)
            print(self.min_amount)

        if self.max_amount == '':
            max_amount = f'SELECT MAX(amount) FROM expenses '

            db = DbConnection().db
            c = db.cursor()

            c.execute(max_amount)
            expense = c.fetchone()
            self.max_amount = expense[0]

        else:
            self.max_amount = float(self.max_amount)

    def execute(self):

        query = 'SELECT * FROM expenses WHERE amount BETWEEN ? AND ? ORDER BY amount DESC'
        data = (self.min_amount, self.max_amount)
        db = DbConnection().db
        c = db.cursor()
        c.execute(query, data)
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')




