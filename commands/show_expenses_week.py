from datetime import date, timedelta
from commands.abs_show_expenses import AbsShowExpenses


class ShowExpensesWeek(AbsShowExpenses):
    name = 'Show expenses - this week'
    start_date = date.today() - timedelta(days=6)
    end_date = date.today() + timedelta(days=1)
