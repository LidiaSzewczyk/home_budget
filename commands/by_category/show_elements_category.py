from amount.expense import Expense
from commands.abs_command import AbsCommand
from commands.helpers import select_table
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowElementsCategory(AbsCommand):
    name = 'Show expenses/income by category'

    def execute(self):
        table = select_table()

        query = f'SELECT * FROM {table[0]}  ORDER BY category'
        elements = DbSelectAll().do(query)

        amount = 0
        obj = table[1]
        for element in elements:
            print(obj(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')



