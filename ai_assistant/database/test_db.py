import sqlite3

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM tickets")

print(cursor.fetchone())

conn.close()