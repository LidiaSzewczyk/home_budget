from datetime import timedelta, datetime

from amount.expense import Expense
from commands.abs_command import AbsCommand
from commands.helpers import select_table, print_elements

from dbs.DbConnection import DbConnection
from dbs.commands_to_db.db_select_all import DbSelectAll
from dbs.commands_to_db.db_select_one import DbSelectOne


class AdvancedFiltering(AbsCommand):
    name = 'Advanced filtering'

    def execute(self):
        table = select_table()

        start_date = input('Provide start date as yyyy-mm-dd\n')
        end_date = input('Provide end date as yyyy-mm-dd\n')

        if start_date == '':
            query_min = f'SELECT MIN(created) FROM {table[0]}'

            element = DbSelectOne().do(query_min)
            start_date = element[0]

        else:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')

        if end_date == '':
            end_date = datetime.now()

        elif len(end_date.strip()) == 10:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

        end_date = end_date + timedelta(days=1)

        category = input('Provide category.\n')

        if category:
            category = f'AND category="{category}"'

        min_amount = input('Provide min amount\n')
        max_amount = input('Provide max amount\n')

        if min_amount == '':
            min_amount = 0

        else:
            min_amount = min_amount.replace(',', '.')
            min_amount = float(min_amount)

        if max_amount == '':
            max_amount = f'SELECT MAX(amount) FROM {table[0]} '

            element = DbSelectOne().do(max_amount)
            max_amount = element[0]

        else:
            max_amount = max_amount.replace(',', '.')
            max_amount = float(max_amount)

        query = f'SELECT * FROM {table[0]} WHERE created BETWEEN ? AND ? {category} AND amount BETWEEN ? AND ? ORDER BY created DESC'
        data = (start_date, end_date, min_amount, max_amount)

        elements = DbSelectAll().do(query, data)

        print_elements(table, elements)
