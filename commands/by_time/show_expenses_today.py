from datetime import date, timedelta

from commands.by_time.abs_show_expenses import AbsShowExpenses


class ShowExpensesToday(AbsShowExpenses):
    name = 'Show expenses - today'
    start_date = date.today()
    end_date = date.today() + timedelta(days=1)
