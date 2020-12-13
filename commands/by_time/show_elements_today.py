from datetime import date, timedelta

from commands.by_time.abs_show_elements import AbsShowElements


class ShowElementsToday(AbsShowElements):
    name = 'Show expenses/income - today'
    start_date = date.today()
    end_date = date.today() + timedelta(days=1)
