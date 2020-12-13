from commands.abs_command import AbsCommand
from commands.helpers import select_table
from dbs.commands_to_db.db_select_one import DbSelectOne
from dbs.commands_to_db.db_commit import DbCommit


class AddNew(AbsCommand):
    name = 'Add new'

    def execute(self):

        table = select_table()

        element_category = input(f'Provide category of {table[0]} \n')
        element_name = input(f'Provide {table[0]} name \n')
        element_amount = input(f'Provide {table[0]} amount\n')

        try:
            element_amount = float(element_amount)
            query = f'INSERT INTO {table[0]} (category, name, amount) VALUES (?, ?, ?)'
            data = (element_category, element_name, element_amount)

            DbCommit().do(query, data)

            query = f'SELECT * FROM {table[0]} WHERE  category=? AND name=? AND amount=? ORDER BY id DESC LIMIT 1'
            data = (element_category, element_name, element_amount,)

            new_element = DbSelectOne().do(query, data)

            obj = table[1]

            print(obj(new_element))

        except ValueError:
            print(f"Incorrect value {element_amount}.")


