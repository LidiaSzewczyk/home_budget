from datetime import timedelta, datetime

from amount.expense import Expense
from commands.abs_command import AbsCommand

from commands.by_time.show_expenses_select_date import ShowExpensesSelectDates
from commands.filter_by_category import FilterByCategory
from dbs.DbConnection import DbConnection


class AdvancedFiltering(AbsCommand):
    name = 'Advanced filtering'

    def execute(self):
        start_date = input('Provide start date as yyyy-mm-dd\n')
        end_date = input('Provide end date as yyyy-mm-dd\n')

        if start_date == '':
            start_date = datetime.now()

            query_min = f'SELECT MIN(created) FROM expenses '

            db = DbConnection().db
            c = db.cursor()

            c.execute(query_min)
            expense = c.fetchone()
            start_date = expense[0]

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
            min_amount = float(min_amount)
            print(min_amount)

        if max_amount == '':
            max_amount = f'SELECT MAX(amount) FROM expenses '

            db = DbConnection().db
            c = db.cursor()

            c.execute(max_amount)
            expense = c.fetchone()
            max_amount = expense[0]

        else:
            max_amount = float(max_amount)

        query = f'SELECT * FROM expenses WHERE created BETWEEN ? AND ? {category} AND amount BETWEEN ? AND ? ORDER BY amount DESC'
        data = (start_date, end_date, min_amount, max_amount)

        db = DbConnection().db
        c = db.cursor()
        c.execute(query, data)
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')
