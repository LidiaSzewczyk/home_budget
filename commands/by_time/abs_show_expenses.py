from abc import ABC

from amount.expense import Expense
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class AbsShowExpenses(AbsCommand, ABC):
    start_date = ''
    end_date = ''

    def execute(self):
        db = DbConnection().db
        c = db.cursor()

        query = 'SELECT * FROM expenses WHERE created BETWEEN ? AND ? ORDER BY created DESC'
        data = (self.start_date, self.end_date)

        c.execute(query, data)
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')



