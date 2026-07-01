from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from app.config import OPENAI_API_KEY

from services.prompt_service import (
    build_system_prompt,
    build_answer_prompt
)


class AIService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            api_key=OPENAI_API_KEY,
            temperature=0
        )

    def generate_sql(self, question, metadata):

        prompt = build_system_prompt(metadata)

        response = self.llm.invoke(
            [
                SystemMessage(content=prompt),
                HumanMessage(content=question)
            ]
        )

        return response.content.strip()

    def generate_answer(self,question,sql, data, total_records):
        """
        Converts SQL results into a natural language response.
        """

        prompt = build_answer_prompt(
                question=question,
                sql=sql,
                data=data,
                total_records=total_records
                   )

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content.strip()