from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class ShowIncome(AbsCommand):
    name = 'Show income'

    def execute(self):
        db = DbConnection().db
        c = db.cursor()

        c.execute('SELECT * FROM income ORDER BY created DESC')
        income = c.fetchall()
        for amount in income:
            print(Income(amount))
