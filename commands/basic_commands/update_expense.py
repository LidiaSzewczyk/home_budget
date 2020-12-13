import math
from datetime import datetime
from commands.abs_command import AbsCommand

from dbs.commands_to_db.db_select_one import DbSelectOne
from dbs.commands_to_db.db_commit import DbCommit
from commands.helpers import select_table


class Update(AbsCommand):
    name = 'Update'

    def execute(self):

        table = select_table()

        element_id = input('Provide id of the expense you want modify.\n')

        try:
            element_id = int(element_id)

            query = f'SELECT * FROM {table[0]} WHERE  id=?'
            data = (element_id,)

            element = DbSelectOne().do(query, data)

            obj = table[1]
            print(obj(element))

        except ValueError:
            print(f"Incorrect value {element_id}.")
        except TypeError:
            print(f"Incorrect value, no id {element_id}.")
        else:
            update_category = input(
                'Select the appropriate number if you want to change:\n '
                'category - 1\n name - 2\n amount - 3\n date of creation - 4\n')

            try:
                update_category = int(math.fabs(int(update_category)))
                [1, 2, 3, 4][update_category - 1]
            except ValueError:
                print(f"Incorrect value {update_category}.")
            except IndexError:
                print(f"Incorrect value, no {update_category}.")
            else:
                if update_category == 1:
                    category = input('Provide new value\n')
                    values = f'category="{category}"'
                elif update_category == 2:
                    name = input('Provide new value\n')
                    values = f'name="{name}"'
                elif update_category == 3:
                    amount = input('Provide new value\n')
                    try:
                        amount = float(amount)
                        values = f'amount="{amount}"'
                    except ValueError:
                        print(f"Incorrect value {amount}.")
                elif update_category == 4:
                    created = input('Provide new value as yyyy-mm-dd.\n')
                    created = datetime.strptime(created, '%Y-%m-%d')
                    values = f'created="{created}"'

                query = f'UPDATE {table[0]} SET {values} WHERE id={element_id}'
                DbCommit().do(query)

                query = f'SELECT * FROM {table[0]} WHERE  id=?'
                updated_element = DbSelectOne().do(query, data)
                print(obj(updated_element))


