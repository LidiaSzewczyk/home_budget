from collections import defaultdict
from commands.abs_command import AbsCommand
from commands.helpers import select_table
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowSumElementsCategory(AbsCommand):
    name = 'Show  sum of expenses/income by category'

    def execute(self):

        table = select_table()

        query = f'SELECT * FROM {table[0]} ORDER BY category'
        elements = DbSelectAll().do(query)

        d = defaultdict(int)
        for idx, category, name, amount, created in elements:
            d[category] += amount

        print(f'Category: sum of {table[0]}')
        for category, amount in d.items():
            print(f'{category}: {" "* (15-len(category) - len(str(amount)))}{amount}')
