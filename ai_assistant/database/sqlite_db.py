import sqlite3
from loader import load_csv

DATABASE_NAME = "tickets.db"


def create_database():

    df = load_csv()

    conn = sqlite3.connect(DATABASE_NAME)

    df.to_sql(
        "tickets",
        conn,
        if_exists="replace",
        index=False
    )

    conn.commit()
    conn.close()

    print("SQLite Database Created Successfully")


if __name__ == "__main__":
    create_database()