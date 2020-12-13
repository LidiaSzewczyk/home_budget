from commands.abs_command import AbsCommand
from commands.cli import Cli
from commands.by_time.show_elements_last_month import ShowElementsLastMonth
from commands.by_time.show_elements_month import ShowElementsMonth
from commands.by_time.show_elements_select_date import ShowElementsSelectDates
from commands.by_time.show_elements_today import ShowElementsToday
from commands.by_time.show_elements_week import ShowElementsWeek
from commands.by_time.show_elements_year import ShowElementsYear


class FilterByTime(AbsCommand):
    name = 'Filter by time'

    def execute(self):
        commands = (ShowElementsToday, ShowElementsWeek, ShowElementsMonth, ShowElementsLastMonth, ShowElementsYear,
                    ShowElementsSelectDates)

        filter = Cli(commands)
        filter.get_user_command()
