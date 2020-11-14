from commands.add_expense import AddExpense
from commands.add_income import AddIncome
from commands.remove_expense import RemoveExpense

a = AddExpense()
a.execute()
a.execute()
c= RemoveExpense()
c.execute()
a.execute()
b= AddIncome()
b.execute()

