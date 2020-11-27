import os
from sqlite3 import OperationalError

from dbs.db_init import db_init
from environment.load_envs import load_envs
from environment.save_env import save_env


def get_path():
    response = input("Do you want to create new db?\n")

    if response.lower() == "yes":
        path = input("Put the db path inside application\n")

        root = os.environ.get('ROOT_DIR')
        abs_path = os.path.join(root, path)

        if os.path.exists(abs_path):
            os.environ['DB_PATH'] = path
            save_env('DB_PATH', path)

    else:
        exit()


def db_validation(db):
    query_expenses = "SELECT id, category, name, amount, created FROM expenses LIMIT 1"
    query_income = "SELECT id, category, name, amount, created FROM expenses LIMIT 1"

    try:
        db.execute(query_expenses)
        db.execute(query_income)
    except OperationalError:
        get_path()
        load_envs()
        db_init()
