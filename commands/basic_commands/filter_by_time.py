from commands.abs_command import AbsCommand
from commands.cli import Cli
from commands.by_time.show_expenses_last_month import ShowExpensesLastMonth
from commands.by_time.show_expenses_month import ShowExpensesMonth
from commands.by_time.show_expenses_select_date import ShowExpensesSelectDates
from commands.by_time.show_expenses_today import ShowExpensesToday
from commands.by_time.show_expenses_week import ShowExpensesWeek
from commands.by_time.show_expenses_year import ShowExpensesYear


class FilterByTime(AbsCommand):
    name = 'Filter by time'

    def execute(self):
        commands = (ShowExpensesToday, ShowExpensesWeek, ShowExpensesMonth, ShowExpensesLastMonth, ShowExpensesYear, ShowExpensesSelectDates)

        filter = Cli(commands)
        filter.get_user_command()
