import math
from datetime import datetime
from amount.expense import Expense
from commands.abs_command import AbsCommand
from commands.users_commands import UsersCommands
from dbs.DbConnection import DbConnection


class UpdateExpense(AbsCommand):
    name = 'Update expense'
    Expense = Expense

    def execute(self):

        expense_id = input('Provide id of the expense you want modify.\n')

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
        else:
            update_category = input(
                'Select the appropriate number if you want to change:\n category - 1\n name - 2\n amount - 3\n date of creation - 4\n')

            try:
                update_category = int(math.fabs(int(update_category)))
                [1, 2, 3, 4][update_category - 1]
            except ValueError:
                print(f"Incorrect value {update_category}.")
            except IndexError:
                print(f"Incorrect value, no {update_category}.")
            else:
                if update_category == 1:
                    category = input('Provide new value\n')
                    values = f'category="{category}"'
                elif update_category == 2:
                    name = input('Provide new value\n')
                    values = f'name="{name}"'
                elif update_category == 3:
                    amount = input('Provide new value\n')
                    try:
                        amount = float(amount)
                        values = f'amount="{amount}"'
                    except ValueError:
                        print(f"Incorrect value {amount}.")
                elif update_category == 4:
                    created = input('Provide new value as yyyy-mm-dd.\n')
                    created = datetime.strptime(created, '%Y-%m-%d')
                    values = f'created="{created}"'

                query = f'UPDATE expenses SET {values} WHERE id={expense_id}'
                c.execute(query)
                db.commit()
                query = f'SELECT * FROM expenses WHERE  id=?'
                db = DbConnection().db
                c = db.cursor()
                c.execute(query, data)
                updated_expense = c.fetchone()
                print(self.Expense(updated_expense))

# TODO ulepszyć
