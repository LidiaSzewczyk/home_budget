import os
import sqlite3

from dbs.db_init import db_init
from dbs.sample_data import insert_sample_data
from environment.save_env import save_env


class DbBuilder:

    def __init__(self):
        db_root = os.environ.get('ROOT_DIR')
        db_path = os.environ.get("DB_PATH")
        db_name = os.environ.get('DB_NAME')

        try:
            self._db_path = os.path.join(db_root, db_path, db_name)
        except TypeError:
            raise ValueError('App configuration is incorrect')

        self._db = None

    @property
    def db_path(self):
        return self._db_path

    @db_path.setter
    def db_path(self, new_val):
        self._db_path = new_val

    @property
    def db(self):
        return self._db

    def check_db_exist(self):
        return os.path.exists(self.db_path)

    def connect_to_db(self):
        self._db = sqlite3.connect(self.db_path)

    def check_db_is_correct(self):
        query_expenses = "SELECT id, category, name, amount, created FROM expenses LIMIT 1"
        query_income = "SELECT id, category, name, amount, created FROM income LIMIT 1"

        try:
            self.db.execute(query_expenses)
            self.db.execute(query_income)

            return True

        except sqlite3.OperationalError:
            return False

    def get_user_path(self):

        user_answer = input("Do you want to create new db?[Y/N]\n")

        if user_answer.lower() == "y":
            user_path = input("Put the db path inside application\n")

            root = os.environ.get('ROOT_DIR')
            try:
                abs_path = os.path.join(root, user_path)
                os.makedirs(abs_path, exist_ok=True)
            except TypeError:
                raise ValueError('Invalid db path')
            except OSError:
                raise ValueError('Invalid db path')

            os.environ['DB_PATH'] = user_path
            save_env('DB_PATH', user_path)
            self.db_path = os.path.join(abs_path, os.environ.get('DB_NAME'))

        else:
            raise ValueError('App configuration is incorrect')

    @staticmethod
    def create_new_db():

        db_init()

        user_answer = input("Do you to put sample data into d?[Y/N]\n")
        if user_answer.lower() == "y":
            insert_sample_data()
