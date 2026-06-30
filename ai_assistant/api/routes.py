from fastapi import APIRouter
from database.database_service import DatabaseService

router = APIRouter()

db = DatabaseService()


@router.get("/")
def home():
    return {
        "message": "Welcome to the AI Support Ticket API"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/tickets/count")
def total_tickets():

    result = db.get_total_tickets()

    return {
        "total_tickets": int(result.iloc[0]["total"])
    }


@router.get("/tickets/open")
def open_tickets():

    result = db.get_open_tickets()

    return result.to_dict(orient="records")


@router.get("/tickets/priority/{priority}")
def ticket_priority(priority: str):

    result = db.get_ticket_by_priority(priority)

    return result.to_dict(orient="records")


@router.get("/ratings")
def ratings():

    result = db.get_average_rating()

    return result.to_dict(orient="records")