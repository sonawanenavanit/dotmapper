from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class HealthResponse(BaseModel):
    status: str


class QueryResponse(BaseModel):
    success: bool
    question: str
    answer: str | None = None
    generated_sql: str | None = None
    data: list
    error: str | None = None