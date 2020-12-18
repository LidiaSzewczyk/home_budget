from amount.expense import Expense
from amount.income import Income
from dbs.commands_to_db.db_select_one import DbSelectOne


def select_table():
    table = input('1. Expenses \n 2. Income \n  Choose command.\n')

    if table.strip() == '1':
        obj = Expense
        return 'expenses', obj
    elif table.strip() == '2':
        obj = Income
        return 'income', obj
    else:
        print("Wrong choice. Try again.")
        select_table()


def print_elements(table, elements):
    amount = 0
    obj = table[1]
    for element in elements:
        print(obj(element))
        amount += obj(element).amount
    print(f'*** Sum of {table[0]}: {round(amount, 2)} ***')


def summary_month(start_date, end_date):
    tables = ['expenses', 'income']
    result = []
    balance = []
    for table in tables:
        query = f'SELECT SUM(amount) FROM {table} WHERE created BETWEEN ? AND ?'
        data = (start_date, end_date)

        element = DbSelectOne().do(query, data)

        if element[0] is None:
            element = 0
        else:
            element = element[0]

        balance.append(element)
        result.append(f'{table}: {element}')

    print(f"{start_date.strftime('%B')}  {'; '.join(result)}; balance: {balance[1] - balance[0]}")
    return balance