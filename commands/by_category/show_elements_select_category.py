from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from commands.helpers import select_table
from dbs.DbConnection import DbConnection
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowElementsSelectCategory(AbsCommand):
    name = 'Select expenses/income by category'

    def execute(self):
        table = select_table()

        category = input('Provide category.\n')

        query = f'SELECT * FROM {table[0]}  WHERE category=? ORDER BY created DESC'
        data = (category,)

        elements = DbSelectAll().do(query, data)

        if elements:
            amount = 0
            for element in elements:
                print(Expense(element))
                amount += Expense(element).amount
            print(f'*** Sum of expenses: {round(amount, 2)} ***')

        else:
            print(f'There is no category: "{category}" in {table[0]}')
