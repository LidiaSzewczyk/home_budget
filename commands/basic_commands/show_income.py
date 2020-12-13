from amount.income import Income
from commands.abs_command import AbsCommand
from dbs.commands_to_db.db_select_all import DbSelectAll


class ShowIncome(AbsCommand):
    name = 'Show all income'

    def execute(self):
        query = 'SELECT * FROM income ORDER BY created DESC'
        income = DbSelectAll().do(query)

        for amount in income:
            print(Income(amount))
