from amount.expense import Expense
from commands.abs_command import AbsCommand


class AddExpense(AbsCommand):
    name = 'Add expense'

    Expense = Expense

    def execute(self):
        expense_category = input('Provide category of expense \n')
        expense_name = input('Provide expense name \n')
        expense_amount = input('Provide expense amount\n')
        new_expense = self.Expense(expense_name, expense_category, expense_amount, self.uuid)
        print(new_expense)
        self.dashboard.append(new_expense)
        print(self.dashboard)
