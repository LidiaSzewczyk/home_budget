from datetime import date, timedelta

from commands.by_time.abs_show_elements import AbsShowElements


class ShowElementsYear(AbsShowElements):
    name = 'Show expenses/income - this year'
    start_date = date.today().replace(day=1, month=1)
    end_date = date.today() + timedelta(days=1)
