from fastapi import APIRouter

from api.models import QueryRequest
from database.database_service import DatabaseService
from services.query_service import QueryService

from services.anomaly_service import AnomalyService

anomaly_service = AnomalyService()

router = APIRouter()

db = DatabaseService()
query_service = QueryService()


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


# ----------------------------
# AI Endpoint
# ----------------------------

@router.post("/query")
def query(request: QueryRequest):

    return query_service.execute(
        request.question
    )


# ----------------------------
# Database Endpoints
# ----------------------------

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

@router.get("/anomalies")
def anomalies():

    return anomaly_service.detect_all()