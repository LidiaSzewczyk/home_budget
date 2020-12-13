from datetime import date

from commands.by_time.abs_show_elements import AbsShowElements


class ShowElementsLastMonth(AbsShowElements):
    name = 'Show expenses - last month'
    start_date = date.today().replace(day=1, month=date.today().month - 1)
    end_date = date.today().replace(day=1)
