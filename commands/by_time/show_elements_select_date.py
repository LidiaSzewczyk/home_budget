from datetime import datetime, timedelta
from commands.by_time.abs_show_elements import AbsShowElements
from commands.helpers import select_table, print_elements
from dbs.commands_to_db.db_select_all import DbSelectAll
from dbs.commands_to_db.db_select_one import DbSelectOne


class ShowElementsSelectDates(AbsShowElements):
    name = 'Show expenses/income - select dates'

    def execute(self):
        table = select_table()

        self.start_date = input('Provide start date as yyyy-mm-dd\n')
        self.end_date = input('Provide end date as yyyy-mm-dd\n')

        if self.start_date == '':
            self.start_date = datetime.now()

            query_min = f'SELECT MIN(created) FROM {table[0]} '
            element = DbSelectOne().do(query_min)

            self.start_date = element[0]

        else:
            self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d')

        if self.end_date == '':
            self.end_date = datetime.now()
        elif len(self.end_date.strip()) == 10:
            self.end_date = datetime.strptime(self.end_date, '%Y-%m-%d')

        self.end_date = self.end_date + timedelta(days=1)

        query = f'SELECT * FROM {table[0]} WHERE created BETWEEN ? AND ? ORDER BY created DESC'
        data = (self.start_date, self.end_date)

        elements = DbSelectAll().do(query, data)
        print_elements(table, elements)
