from commands.add_expense import AddExpense
from commands.add_income import AddIncome
from commands.cli import Cli
from commands.filter_by_time import FilterByTime
from commands.remove import Remove
from commands.show_all import ShowAll
from commands.update import Update


commands = (AddExpense, AddIncome, FilterByTime,  Update, Remove, ShowAll)

app = Cli(commands)
app.run()
