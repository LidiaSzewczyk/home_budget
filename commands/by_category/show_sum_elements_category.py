from collections import defaultdict
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowSumExpensesCategory(AbsCommand):
    name = 'Show  sum of expenses by category'

    def execute(self):

        query = 'SELECT * FROM expenses ORDER BY category'
        expenses = DbSelectAll().do(query)

        d = defaultdict(int)
        for idx, category, name, amount, created in expenses:
            d[category] += amount

        print('Category: sum of expenses')
        for category, amount in d.items():
            print(f'{category}: {amount}')
