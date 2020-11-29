from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class ShowAll(AbsCommand):
    name = 'Show all'

    def execute(self):

        db = DbConnection().db
        c = db.cursor()

        c.execute('SELECT * FROM expenses')
        expenses = c.fetchall()

        for amount in expenses:
            expense = Expense(amount)
            if expense in self.dashboard:
                self.dashboard.append(expense)

        c.execute('SELECT * FROM income')
        income = c.fetchall()
        for amount in income:
            self.dashboard.append(Income(amount))
        print(set(self.dashboard))
        for amount in set(self.dashboard):
            print(amount)
# TODO poprawić bo się powtarza