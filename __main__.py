from commands.filter_by_amount import FilterByAmount
from commands.advancedfiltering import AdvancedFiltering
from commands.filter_by_category import FilterByCategory
from commands.show_expenses import ShowExpenses
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

commands = (AddExpense, AddIncome,  UpdateExpense, Remove, FilterByTime, FilterByCategory, FilterByAmount, AdvancedFiltering, ShowExpenses, ShowIncome, ShowAll)

app = Cli(commands)
app.run()
