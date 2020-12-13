from commands.abs_command import AbsCommand
from commands.helpers import select_table
from dbs.commands_to_db.db_commit import DbCommit
from dbs.commands_to_db.db_select_one import DbSelectOne


class Remove(AbsCommand):
    name = 'Remove'

    def execute(self):

        table = select_table()

        element_id = input('Provide expense id you want to remove. \n')

        try:
            element_id = int(element_id)

            query = f'SELECT * FROM {table[0]} WHERE  id=?'
            data = (element_id,)

            element = DbSelectOne().do(query, data)
            obj = table[1]
            print(obj(element))

            confirm = input('To confirm deletion provide "Y".').lower().strip()

            if confirm == 'y':
                query_delete = f'DELETE FROM  {table[0]} WHERE id = ?'
                data = (element_id,)

                DbCommit().do(query_delete, data)
                print('The expense has been removed.')

        except ValueError:
            print(f"Incorrect value {element_id}.")
        except TypeError:
            print(f"Incorrect value, no id {element_id}.")
