from amount.expense import Expense
from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class ShowExpensesSelectCategory(AbsCommand):
    name = 'Select expenses by category'

    def execute(self):
        category = input('Provide category.\n')
        query ='SELECT * FROM expenses WHERE category=? ORDER BY created DESC'
        data = (category,)

        db = DbConnection().db
        c = db.cursor()

        c.execute(query, data)
        expenses = c.fetchall()

        amount = 0
        for element in expenses:
            print(Expense(element))
            amount += Expense(element).amount
        print(f'*** Sum of expenses: {round(amount, 2)} ***')



