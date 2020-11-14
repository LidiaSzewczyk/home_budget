from amount.expense import Expense
from amount.income import Income
from uuid.uuid import UUID

uuid = UUID()
my_iter = iter(uuid)

expense = Expense('milk', 'food', 2, my_iter)
print(expense)

income = Income('clinic', 'Ala', 2000, my_iter)
print(income)

