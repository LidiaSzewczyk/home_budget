from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class AddIncome(AbsCommand):
    name = 'Add income'

    Income = Income

    def execute(self):
        income_category = input('Provide category of income \n')
        income_name = input('Provide income name \n')
        income_amount = input('Provide income amount\n')

        query = 'INSERT INTO income (category, name, amount) VALUES (?, ?, ?)'
        data = (income_category, income_name, income_amount)
        db = DbConnection().db
        c = db.cursor()

        c.execute(query, data)
        db.commit()

        query = f'SELECT * FROM income WHERE  category=? AND name=? AND amount=? ORDER BY id DESC LIMIT 1'
        data = (income_category, income_name, income_amount,)

        db = DbConnection().db
        c = db.cursor()

        c.execute(query, data)
        new_expense = c.fetchone()

        new_expense = self.Income(new_expense)

        print(new_expense)
