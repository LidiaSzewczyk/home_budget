from commands.show_expenses import ShowExpenses
from commands.show_expenses_amount import ShowExpensesAmount
from commands.show_expenses_category import ShowExpensesCategory
from commands.show_expenses_select_amount import ShowExpensesSelectAmount
from commands.show_expenses_select_category import ShowExpensesSelectCategory
from commands.show_income import ShowIncome
from commands.update_expense import UpdateExpense
from environment.load_envs import load_envs

load_envs()

from commands.add_expense import AddExpense
from commands.add_income import AddIncome
from commands.cli import Cli
from commands.filter_by_time import FilterByTime
from commands.remove import Remove
from commands.show_all import ShowAll

commands = (AddExpense, AddIncome, FilterByTime, UpdateExpense, Remove, ShowExpenses, ShowExpensesCategory,
            ShowExpensesSelectCategory, ShowExpensesSelectAmount, ShowExpensesAmount, ShowIncome, ShowAll)

app = Cli(commands)
app.run()
