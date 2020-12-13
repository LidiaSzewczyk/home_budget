from dbs.DbConnection import DbConnection


def insert_sample_data():

    db = DbConnection().db
    cursor = db.cursor()

    expenses = [
        ("food", "bread", 5),
        ("transport", "fuel", 200),
        ("food", "apples", 7),
        ("kids", "toys", 70),
        ("transport", "bus", 3.5)
    ]

    cursor.executemany("INSERT INTO expenses (category, name, amount) VALUES (?, ?, ?)", expenses)

    income = [
        ("Anna", "project", 500),
        ("Tom", "salary", 3000),
        ("Anna", "salary", 3000)
    ]

    cursor.executemany("INSERT INTO income (category, name, amount) VALUES (?, ?, ?)", income)

    db.commit()
    db.close()

    print("Data has been added.")


if __name__ == '__main__':
    insert_sample_data()
