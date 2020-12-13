class DbCheck:
    def __init__(self, builder):
        self._builder = builder

    def preflight_check_db(self):
        if self._builder.check_db_exist():
            self._builder.connect_to_db()
            if self._builder.check_db_is_correct():
                return
        self._builder.get_user_path()
        self._builder.create_new_db()
        self._builder.connect_to_db()