import math

# [1, 2, 3, 4][6 - 1]

# print(math.fabs(1000))
from datetime import datetime, date, timedelta
# a =date.today() + timedelta(days=1)
# datetime.datetime.combine(date.today(), dat)
# print(a.strftime(' %d    %H:%M'))
# print(datetime.now().strftime(' %d    %H:%M'))

start_date = date.today().replace(day=1)
print(start_date)
print(type(date.today().month))
