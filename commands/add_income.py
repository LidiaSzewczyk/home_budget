from amount.income import Income
from commands.abs_command import AbsCommand


class AddIncome(AbsCommand):
    name = 'Add income'

    Income = Income

    def execute(self):
        income_category = input('Provide category of income \n')
        income_name = input('Provide income name \n')
        income_amount = input('Provide income amount\n')
        new_income = self.Income(income_name, income_category, income_amount, self.uuid)
        print(new_income)
        self.dashboard.append(new_income)
        print(self.dashboard)
