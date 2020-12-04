from datetime import datetime, date, timedelta

from commands.abs_command import AbsCommand
from commands.abs_show_expenses import AbsShowExpenses
from commands.show_expenses_last_month import ShowExpensesLastMonth
from commands.show_expenses_month import ShowExpensesMonth
from commands.show_expenses_select_date import ShowExpensesSelectDates
from commands.show_expenses_today import ShowExpensesToday
from commands.show_expenses_week import ShowExpensesWeek
from commands.show_expenses_year import ShowExpensesYear
from commands.users_commands import UsersCommands


class FilterByTime(AbsCommand):
    name = 'Filter by time'

    def execute(self):
        command_id = int(input(
            'Select the appropriate number if you want to display:\n this day - 1\n this week - 2\n this month - 3\n last month - 4\n this year - 5\n select dates - 6\n')
        )

        if command_id == 1:
            ShowExpensesToday().execute()


        elif command_id == 2:
            ShowExpensesWeek().execute()


        elif command_id == 3:
            ShowExpensesMonth().execute()

        elif command_id == 4:
            ShowExpensesLastMonth().execute()


        elif command_id == 5:
            ShowExpensesYear().execute()

        elif command_id == 6:
            ShowExpensesSelectDates().execute()
