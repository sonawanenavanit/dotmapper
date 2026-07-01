from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY

from services.prompt_service import (
    build_system_prompt,
    build_answer_prompt
)


class AIService:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=GROQ_API_KEY,
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

    def generate_answer(
        self,
        question,
        sql,
        data,
        total_records
    ):

        prompt = build_answer_prompt(
            question,
            sql,
            data,
            total_records
        )

        response = self.llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content.strip()