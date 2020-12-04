from commands.abs_command import AbsCommand
from dbs.DbConnection import DbConnection
from amount.expense import Expense


class Remove(AbsCommand):
    name = 'Remove'
    Expense = Expense

    def execute(self):
        expense_id = input('Provide expense id you want to remove. \n')

        try:
            expense_id = int(expense_id)

            query = f'SELECT * FROM expenses WHERE  id=?'
            data = (expense_id,)

            db = DbConnection().db
            c = db.cursor()

            c.execute(query, data)
            expense = c.fetchone()
            print(self.Expense(expense))

        except ValueError:
            print(f"Incorrect value {expense_id}.")
        except TypeError:
            print(f"Incorrect value, no id {expense_id}.")

        confirm = input('To confirm deletion provide "Y".').lower().strip()

        if confirm == 'y':
            query_delete = 'DELETE FROM  expenses WHERE id = ?'
            data = (expense_id,)

            db = DbConnection().db
            c = db.cursor()

            c.execute(query_delete, data)
            db.commit()
            print('The expense has been removed.')

