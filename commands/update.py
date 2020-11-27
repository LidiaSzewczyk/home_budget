import math
from datetime import datetime

from commands.abs_command import AbsCommand
from commands.users_commands import UsersCommands


class Update(AbsCommand):
    name = 'Update'

    def execute(self):

        user_command = UsersCommands()
        expense_id = user_command.id_to_update

        try:
            expense_id = int(expense_id)
            expense = list(filter(lambda e: e.uuid == expense_id, self.dashboard))[0]
        except ValueError:
            print(f"Incorrect value {expense_id}.")
        except IndexError:
            print(f"Incorrect value, no id {expense_id}.")
        else:
            # expense = list(filter(lambda e: e.uuid == expense_id, self.dashboard))[0]
            update_category = user_command.update_category

            try:
                update_category = int(math.fabs(int(update_category)))
                [1, 2, 3, 4][update_category - 1]
            except ValueError:
                print(f"Incorrect value {update_category}.")
            except IndexError:
                print(f"Incorrect value, no {update_category}.")
            else:
                if update_category == 1:
                    expense.category = user_command.update_content
                elif update_category == 2:
                    expense.name = user_command.update_content
                elif update_category == 3:
                    expense.amount = user_command.update_content
                elif update_category == 4:
                    expense.created = datetime.strptime(user_command.update_content_time, '%Y-%m-%d')

#  TODO poprawić i dopisać
