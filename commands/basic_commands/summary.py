from datetime import date, timedelta

from commands.abs_command import AbsCommand
from commands.helpers import summary_month
from dbs.DbConnection import DbConnection
from dbs.commands_to_db.db_select_one import DbSelectOne


class Summary(AbsCommand):
    name = 'Summary'

    def execute(self):
        result = []
        for month in range(2, date.today().month + 1):
            start_date = date.today().replace(day=1, month=month - 1)
            end_date = date.today().replace(day=1, month=month)

            balance = summary_month(start_date, end_date)
            result.append(balance)

        start_date = date.today().replace(day=1)
        end_date = date.today() + timedelta(days=1)

        balance = summary_month(start_date, end_date)
        result.append(balance)

        expenses = sum([x[0] for x in result])
        income = sum([x[1] for x in result])
        print(f"This year  expenses: {expenses}; income: {income}; balance: {round(income-expenses, 2)}")

