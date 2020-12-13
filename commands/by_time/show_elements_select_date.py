from datetime import datetime, timedelta

from commands.by_time.abs_show_elements import AbsShowElements
from dbs.DbConnection import DbConnection
from amount.expense import Expense


class ShowElementsSelectDates(AbsShowElements):
    name = 'Show expenses/income - select dates'
    Expense = Expense

    def execute(self):
        self.start_date = input('Provide start date as yyyy-mm-dd\n')
        self.end_date = input('Provide end date as yyyy-mm-dd\n')

        if self.start_date == '':
            self.start_date = datetime.now()

            query_min = f'SELECT MIN(created) FROM expenses '

            db = DbConnection().db
            c = db.cursor()

            c.execute(query_min)
            expense = c.fetchone()
            self.start_date = expense[0]

        else:
            self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d')

        if self.end_date == '':
            self.end_date = datetime.now()
        elif len(self.end_date.strip()) == 10:
            self.end_date = datetime.strptime(self.end_date, '%Y-%m-%d')

        self.end_date = self.end_date + timedelta(days=1)

        super().execute()
