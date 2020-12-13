from datetime import date, timedelta
from commands.by_time.abs_show_elements import AbsShowElements


class ShowElementsWeek(AbsShowElements):
    name = 'Show expenses/income - this week'
    start_date = date.today() - timedelta(days=6)
    end_date = date.today() + timedelta(days=1)
