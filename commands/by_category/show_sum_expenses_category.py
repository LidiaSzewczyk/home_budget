from collections import defaultdict, Counter

from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class ShowSumExpensesCategory(AbsCommand):
    name = 'Show  sum of expenses by category'

    def execute(self):

        db = DbConnection().db
        c = db.cursor()

        c.execute('SELECT * FROM expenses ORDER BY category')
        expenses = c.fetchall()

        d = defaultdict(int)
        for idx, category, name, amount, created in expenses:
            d[category] += amount

        print('Category: sum of expenses')
        for category, amount in d.items():
            print(f'{category}: {amount}')
