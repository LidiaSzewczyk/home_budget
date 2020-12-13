from dbs.commands_to_db.abs_command_to_db import AbsDb


class DbSelectAll(AbsDb):

    def do(self, query, *args):
        self.cursor.execute(query, *args)
        return self.cursor.fetchall()
