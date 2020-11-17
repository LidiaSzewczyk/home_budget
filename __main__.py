from commands.add_expense import AddExpense
from commands.add_income import AddIncome
from commands.cli import Cli
from commands.remove_expense import RemoveExpense
from commands.show_all import ShowAll
from commands.update_expense import UpdateExpense


commands = (AddExpense, AddIncome, RemoveExpense, UpdateExpense, ShowAll)

app = Cli(commands)
app.run()
