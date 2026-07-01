from services.ai_service import AIService
from services.metadata_service import MetadataService
from services.sql_service import SQLService
from database.database_service import DatabaseService


class QueryService:

    def __init__(self):

        self.ai = AIService()
        self.db = DatabaseService()
        self.metadata = MetadataService()

    def execute(self, question):

        try:

            metadata = self.metadata.get_metadata()

            question = question.strip()

            # Remove surrounding quotes
            question = question.strip('"')
            question = question.strip("'")

            # Remove common bullet characters
            question = question.lstrip("•*- ")

            # Remove accidental leading dots
            question = question.lstrip(".")
            

            sql = self.ai.generate_sql(
                question=question,
                metadata=metadata
            )

            sql = SQLService.clean_sql(sql)

            SQLService.validate(sql)

            print("\nGenerated SQL:")
            print(sql)

            result = self.db.execute_query(sql)

            records = result.to_dict(orient="records")
            total_records = len(records)

            answer = self.ai.generate_answer(
                                question=question,
                                sql=sql,
                                data=records,
                                total_records=total_records
                               )

            return {
                    "success": True,
                     "question": question,
                    "generated_sql": sql,
                    "answer": answer,
                    "data": records,
                    "total_records": total_records
                    }

        except Exception as e:

            return {
                "success": False,
                "question": question,
                "error": str(e)
            }