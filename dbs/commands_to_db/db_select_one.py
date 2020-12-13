from dbs.commands_to_db.abs_command_to_db import AbsDb


class DbSelectOne(AbsDb):

    def do(self, query, *args):
        self.cursor.execute(query, *args)
        return self.cursor.fetchone()
