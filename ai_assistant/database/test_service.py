from database_service import DatabaseService

db = DatabaseService()

print("\nTotal Tickets")
print(db.get_total_tickets())

print("\nOpen Tickets")
print(db.get_open_tickets().head())

print("\nCritical Tickets")
print(db.get_ticket_by_priority("Critical").head())

print("\nAverage Ratings")
print(db.get_average_rating())