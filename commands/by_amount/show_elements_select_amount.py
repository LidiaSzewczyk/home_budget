from commands.abs_command import AbsCommand
from commands.helpers import select_table, print_elements
from amount.expense import Expense
from dbs.commands_to_db.db_select_all import DbSelectAll
from dbs.commands_to_db.db_select_one import DbSelectOne


class ShowElementsSelectAmount(AbsCommand):
    name = 'Show expenses/income - select amounts'
    Expense = Expense

    def execute(self):
        table = select_table()

        min_amount = input('Provide min amount\n')
        max_amount = input('Provide max amount\n')

        if min_amount == '':
            min_amount = 0

        else:
            min_amount = min_amount.replace(',', '.')
            min_amount = float(min_amount)


        if max_amount == '':
            max_amount = f'SELECT MAX(amount) FROM {table[0]}'

            element = DbSelectOne().do(max_amount)

            max_amount = element[0]

        else:
            max_amount = max_amount.replace(',', '.')
            max_amount = float(max_amount)

        query = f'SELECT * FROM {table[0]} WHERE amount BETWEEN ? AND ? ORDER BY amount DESC'
        data = (min_amount, max_amount)

        elements = DbSelectAll().do(query, data)

        print_elements(table, elements)
