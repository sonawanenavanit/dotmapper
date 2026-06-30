import sqlite3

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM tickets")

count = cursor.fetchone()[0]

print(f"Total Tickets : {count}")

cursor.execute("""
SELECT priority,
COUNT(*)
FROM tickets
GROUP BY priority
""")

print("\nPriority Distribution")

for row in cursor.fetchall():
    print(row)

conn.close()