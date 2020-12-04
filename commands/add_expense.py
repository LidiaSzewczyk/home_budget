from amount.expense import Expense
from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection


class AddExpense(AbsCommand):
    name = 'Add expense'

    Expense = Expense

    def execute(self):
        expense_category = input('Provide category of expense \n')
        expense_name = input('Provide expense name \n')

        expense_amount = input('Provide expense amount\n')
        try:
            expense_amount = float(expense_amount)
        except ValueError:
            print(f"Incorrect value {expense_amount}.")


        query = 'INSERT INTO expenses (category, name, amount) VALUES (?, ?, ?)'
        data = (expense_category, expense_name, expense_amount)
        db = DbConnection().db
        c = db.cursor()

        c.execute(query, data)
        db.commit()

        query = f'SELECT * FROM expenses WHERE  category=? AND name=? AND amount=? ORDER BY id DESC LIMIT 1'
        data = (expense_category, expense_name, expense_amount,)

        db = DbConnection().db
        c = db.cursor()

        c.execute(query, data)
        new_expense = c.fetchone()

        new_expense = self.Expense(new_expense)

        print(new_expense)
