# 🤖 AI Support Ticket Assistant

An AI-powered Support Ticket Analysis System that allows users to query customer support ticket data using natural language. The application converts user questions into SQLite queries using a Large Language Model (LLM), executes them securely, and presents the results through a FastAPI backend and a Streamlit web interface.

---

## Features

- Natural Language to SQL using LLM (Groq Llama 3.3 70B)
- Secure SQL Generation with validation
- SQLite Database
- CSV Data Ingestion
- FastAPI REST API
- Streamlit Web Interface
- Automatic Metadata Extraction
- AI Generated Natural Language Responses
- Anomaly Detection
- Modular Service-Oriented Architecture

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- SQLite
- Pandas
- LangChain
- Groq API
- Pydantic

---

# Project Structure

```
DotMapper/
│
├── api/
│   ├── models.py
│   └── routes.py
│
├── app/
│   └── config.py
│
├── database/
│   ├── database_service.py
│   ├── loader.py
│   └── sqlite_db.py
│
├── data/
│   └── support_tickets.csv
│
├── services/
│   ├── ai_service.py
│   ├── anomaly_service.py
│   ├── metadata_service.py
│   ├── prompt_service.py
│   ├── query_service.py
│   └── sql_service.py
│
├── tests/
│
├── ui/
│   └── app.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# Architecture

```
                Streamlit UI
                      │
                      ▼
               FastAPI Backend
                      │
          ┌───────────┴───────────┐
          │                       │
    Query Service          Anomaly Service
          │
          ▼
      AI Service
          │
          ▼
 Prompt Engineering
          │
          ▼
     Groq LLM
          │
          ▼
     Generated SQL
          │
          ▼
     SQL Validation
          │
          ▼
        SQLite
          │
          ▼
      Query Result
          │
          ▼
 AI Generated Response
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository_url>

cd DotMapper
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```text
GROQ_API_KEY=your_groq_api_key
```

---

# Running the Application

## Start FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit UI

Open another terminal.

```bash
streamlit run ui/app.py
```

Application URL

```
http://localhost:8501
```

---

# REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| POST | /query | Natural Language Query |
| GET | /anomalies | Detect Anomalies |

---

# Example Questions

- How many tickets are currently open?
- Show all Critical tickets.
- Which agent resolved the most tickets?
- Which category has the highest average resolution time?
- Show unresolved Billing tickets.
- What is the average customer rating?
- List all tickets with customer rating below 3.
- Show all High priority tickets.

---

# Anomaly Detection

The application detects the following anomalies:

- Tickets with long resolution time (>12 hours)
- Tickets with slow response time (>4 hours)
- High/Critical unresolved tickets
- Tickets with customer rating less than or equal to 2

---

# Security

To improve security, generated SQL is validated before execution.

The validator ensures:

- Only SELECT statements are allowed
- INSERT is blocked
- UPDATE is blocked
- DELETE is blocked
- DROP is blocked
- ALTER is blocked
- CREATE is blocked
- TRUNCATE is blocked
- PRAGMA is blocked
- ATTACH is blocked

---

# AI Workflow

```
User Question
      │
      ▼
Metadata Extraction
      │
      ▼
Prompt Engineering
      │
      ▼
Groq LLM
      │
      ▼
Generated SQL
      │
      ▼
SQL Validation
      │
      ▼
SQLite Execution
      │
      ▼
Query Result
      │
      ▼
Natural Language Response
```

---

# Future Improvements

- Docker Deployment
- Authentication
- Conversation Memory
- Support for Multiple Databases
- Query History
- Charts and Visual Analytics
- Export Results to CSV

---

# Author

Navanit Sonawane