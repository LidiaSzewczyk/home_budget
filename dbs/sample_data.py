import sqlite3
import os


def insert_sample_data():
    db_name = 'budget.db'
    db_path = os.path.join(os.path.dirname(__file__), '..', db_name)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    expenses = [
        ("food", "bread", 5),
        ("transport", "fuel", 200),
        ("food", "apples", 7),
        ("kids", "toys", 70),
        ("transport", "bus", 3.5)
    ]

    c.executemany("INSERT INTO expenses (category, name, amount) VALUES (?, ?, ?)", expenses)

    income = [
        ("Anna", "project", 500),
        ("Tom", "salary", 3000),
        ("Anna", "salary", 3000)
    ]

    c.executemany("INSERT INTO income (category, name, amount) VALUES (?, ?, ?)", income)

    conn.commit()
    conn.close()

    print("data added")


if __name__ == '__main__':
    insert_sample_data()
