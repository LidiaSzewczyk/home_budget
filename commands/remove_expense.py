from commands.abs_command import AbsCommand


class RemoveExpense(AbsCommand):
    name = 'Remove expense'

    def execute(self):
        expense_id = input('Provide expense id you want to remove. \n')

        try:
            expense_id = int(expense_id)

        except ValueError:
            print(f"Incorrect value {expense_id}.")
        try:
            expense = list(filter(lambda e: e.uuid == expense_id, self.dashboard))
            self.dashboard.remove(expense[0])
            print(self.dashboard)
        except IndexError:
            print(f"Incorrect value {expense_id}.")

