from datetime import date, timedelta

from commands.abs_show_expenses import AbsShowExpenses


class ShowExpensesToday(AbsShowExpenses):
    name = 'Show expenses - today'
    start_date = date.today()
    end_date = date.today() + timedelta(days=1)
