from abc import ABC
from commands.abs_command import AbsCommand
from commands.helpers import print_elements, select_table
from dbs.commands_to_db.db_select_all import DbSelectAll


class AbsShowElements(AbsCommand, ABC):
    start_date = ''
    end_date = ''

    def execute(self):
        table = select_table()

        query = f'SELECT * FROM {table[0]} WHERE created BETWEEN ? AND ? ORDER BY created DESC'
        data = (self.start_date, self.end_date)

        elements = DbSelectAll().do(query, data)
        print_elements(table, elements)





