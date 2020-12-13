from dbs.db_builder import DbBuilder
from dbs.db_check import DbCheck
from environment.load_envs import load_envs

load_envs()
db_builder = DbCheck(DbBuilder())
db_builder.preflight_check_db()

from commands.basic_commands.filter_by_amount import FilterByAmount
from commands.basic_commands.advancedfiltering import AdvancedFiltering
from commands.basic_commands.filter_by_category import FilterByCategory
from commands.basic_commands.show_expenses import ShowExpenses
from commands.basic_commands.show_income import ShowIncome
from commands.basic_commands.summary import Summary
from commands.basic_commands.update_expense import Update
from commands.basic_commands.add_new import AddNew
from commands.cli import Cli
from commands.basic_commands.filter_by_time import FilterByTime
from commands.basic_commands.remove import Remove
from commands.basic_commands.show_all import ShowAll

commands = (
    AddNew, Update, Remove, FilterByTime, FilterByCategory,
    FilterByAmount, AdvancedFiltering, ShowExpenses, ShowIncome,
    ShowAll, Summary)

app = Cli(commands)
app.run()
