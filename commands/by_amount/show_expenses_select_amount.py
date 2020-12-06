from commands.abs_command import AbsCommand

from dbs.DbConnection import DbConnection
from amount.expense import Expense


class ShowExpensesSelectAmount(AbsCommand):
    name = 'Show expenses - select amounts'
    Expense = Expense

    def execute(self):

        min_amount = input('Provide min amount\n')
        max_amount = input('Provide max amount\n')

        if min_amount == '':
            min_amount = 0

        else:
            min_amount = float(min_amount)
            print(min_amount)

        if max_amount == '':
            max_amount = f'SELECT MAX(amount) FROM expenses '

            db = DbConnection().db
            c = db.cursor()

            c.execute(max_amount)
            expense = c.fetchone()
            max_amount = expense[0]

        else:
            max_amount = float(max_amount)



        query = 'SELECT * FROM expenses WHERE amount BETWEEN ? AND ? ORDER BY amount DESC'
        data = (min_amount, max_amount)
        db = DbConnection().db
        c = db.cursor()
        c.execute(query, data)
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')




