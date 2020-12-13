from commands.abs_command import AbsCommand
from commands.helpers import select_table, print_elements
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowElementsCategory(AbsCommand):
    name = 'Show expenses/income by category'

    def execute(self):
        table = select_table()

        query = f'SELECT * FROM {table[0]}  ORDER BY category'
        elements = DbSelectAll().do(query)

        print_elements(table, elements)




