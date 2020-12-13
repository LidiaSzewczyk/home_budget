import sqlite3
import os


def db_init():
    db_path = os.environ.get("DB_PATH")
    db_name = os.environ.get('DB_NAME')
    db_root = os.environ.get('ROOT_DIR')
    db_path = os.path.join(db_root, db_path, db_name)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS expenses")
    c.execute("DROP TABLE IF EXISTS income")

    c.execute("""CREATE TABLE expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        name TEXT,
        amount FLOAT,
        created TEXT default (datetime('now', 'localtime'))
    )""")

    c.execute("""CREATE TABLE income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        name TEXT,
        amount FLOAT,
        created TEXT default (datetime('now', 'localtime'))
    )""")

    conn.commit()
    conn.close()

    print("Database is initialized")


if __name__ == "__main__":
    db_init()
