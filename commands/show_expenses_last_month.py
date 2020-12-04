from datetime import date

from commands.abs_show_expenses import AbsShowExpenses


class ShowExpensesLastMonth(AbsShowExpenses):
    name = 'Show expenses - last month'
    start_date = date.today().replace(day=1, month=date.today().month - 1)
    end_date = date.today().replace(day=1)
