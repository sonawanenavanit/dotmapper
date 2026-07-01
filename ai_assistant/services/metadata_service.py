from database.database_service import DatabaseService


class MetadataService:

    def __init__(self):
        self.db = DatabaseService()
        self.metadata = self._load_metadata()

    def get_unique_values(self, column):

        query = f"""
        SELECT DISTINCT {column}
        FROM tickets
        WHERE {column} IS NOT NULL
        ORDER BY {column}
        """

        df = self.db.execute_query(query)

        return df[column].tolist()

    def _load_metadata(self):

        return {

            "status": {
                "type": "TEXT",
                "values": self.get_unique_values("status")
            },

            "priority": {
                "type": "TEXT",
                "values": self.get_unique_values("priority")
            },

            "category": {
                "type": "TEXT",
                "values": self.get_unique_values("category")
            },

            "agent_id": {
                "type": "TEXT",
                "values": self.get_unique_values("agent_id")
            },

            "response_time_hrs": {
                "type": "REAL"
            },

            "resolution_time_hrs": {
                "type": "REAL"
            },

            "customer_rating": {
                "type": "INTEGER"
            },

            "created_at": {
                "type": "DATETIME"
            }

        }

    def get_metadata(self):
        return self.metadata