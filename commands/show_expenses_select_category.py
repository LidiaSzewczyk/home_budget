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

        for amount in expenses:
            print(Expense(amount))



