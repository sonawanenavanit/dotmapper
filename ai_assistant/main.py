from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Support Ticket AI API",
    description="AI Engineer Assessment",
    version="1.0"
)

app.include_router(router)