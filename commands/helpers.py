from amount.expense import Expense
from amount.income import Income


def select_table():
    table = int(input('1. Expenses \n 2. Income \n  Choose command.\n'))

    if table == 1:
        obj = Expense
        return 'expenses', obj
    elif table == 2:
        obj = Income
        return 'income', obj
    else:
        print("Wrong number.")
        select_table()

