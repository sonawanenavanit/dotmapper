import pandas as pd

from database.database_service import DatabaseService


class AnomalyService:

    def __init__(self):
        self.db = DatabaseService()

    def long_resolution_time(self):

        query = """
        SELECT *
        FROM tickets
        WHERE resolution_time_hrs > 12
        ORDER BY resolution_time_hrs DESC
        """

        return self.db.execute_query(query)

    def slow_response_time(self):

        query = """
        SELECT *
        FROM tickets
        WHERE response_time_hrs > 4
        ORDER BY response_time_hrs DESC
        """

        return self.db.execute_query(query)

    def old_unresolved_high_priority(self):

        query = """
        SELECT *
        FROM tickets
        WHERE priority IN ('High', 'Critical')
        AND status != 'Resolved'
        ORDER BY priority
        """

        return self.db.execute_query(query)

    def low_customer_rating(self):

        query = """
        SELECT *
        FROM tickets
        WHERE customer_rating <= 2
        ORDER BY customer_rating ASC
        """

        return self.db.execute_query(query)

    def dataframe_to_records(self, df):
        """
        Converts a DataFrame into JSON-safe records.
        Replaces NaN values with None.
        """

        df = df.astype(object)
        df = df.where(pd.notnull(df), None)

        return df.to_dict(orient="records")

    def detect_all(self):

        long_resolution = self.long_resolution_time()

        slow_response = self.slow_response_time()

        old_unresolved = self.old_unresolved_high_priority()

        low_rating = self.low_customer_rating()

        return {

            "long_resolution_time":
                self.dataframe_to_records(long_resolution),

            "slow_response_time":
                self.dataframe_to_records(slow_response),

            "old_unresolved_high_priority":
                self.dataframe_to_records(old_unresolved),

            "low_customer_rating":
                self.dataframe_to_records(low_rating)

        }