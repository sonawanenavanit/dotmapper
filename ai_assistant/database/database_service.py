import sqlite3
import pandas as pd


class DatabaseService:

    def __init__(self):
        self.db_path = "tickets.db"

    def execute_query(self, query, params=None):

        conn = sqlite3.connect(self.db_path)

        df = pd.read_sql_query(
            query,
            conn,
            params=params
        )

        conn.close()

        return df

    def get_total_tickets(self):

        query = """
        SELECT COUNT(*) AS total
        FROM tickets
        """

        return self.execute_query(query)

    def get_open_tickets(self):

        query = """
        SELECT *
        FROM tickets
        WHERE status = ?
        """

        return self.execute_query(query, ("Open",))

    def get_ticket_by_priority(self, priority):

        query = """
        SELECT *
        FROM tickets
        WHERE priority = ?
        """

        return self.execute_query(query, (priority,))

    def get_average_rating(self):

        query = """
        SELECT
            agent_id,
            ROUND(AVG(customer_rating), 2) AS avg_rating
        FROM tickets
        GROUP BY agent_id
        ORDER BY avg_rating DESC
        """

        return self.execute_query(query)