from datetime import date, timedelta

from commands.by_time.abs_show_expenses import AbsShowExpenses


class ShowExpensesMonth(AbsShowExpenses):
    name = 'Show expenses - this month'
    start_date = date.today().replace(day=1)
    end_date = date.today() + timedelta(days=1)
