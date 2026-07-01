DATABASE_SCHEMA = """
Table Name: tickets

Columns

ticket_id (TEXT)
created_at (DATETIME)
category (TEXT)
priority (TEXT)
status (TEXT)
response_time_hrs (REAL)
resolution_time_hrs (REAL)
agent_id (TEXT)
customer_rating (INTEGER)
issue_summary (TEXT)
"""


COLUMN_DESCRIPTIONS = """
Column Descriptions

ticket_id:
Unique ticket identifier.

created_at:
Date and time when the ticket was created.

category:
Category of the issue reported by the customer.

priority:
Urgency level of the ticket.

status:
Current ticket status.

response_time_hrs:
Hours taken for the first response from the support team.

resolution_time_hrs:
Hours taken to completely resolve the ticket.

agent_id:
Support agent assigned to the ticket.

customer_rating:
Customer satisfaction rating after ticket resolution (1 to 5).

issue_summary:
Short summary describing the customer's issue.
"""


def build_system_prompt(metadata):

    return f"""
You are an expert SQLite SQL generator.

Your task is to convert a user's natural language question into a valid SQLite SELECT query.

==========================
DATABASE SCHEMA
==========================

{DATABASE_SCHEMA}

==========================
COLUMN DESCRIPTIONS
==========================

{COLUMN_DESCRIPTIONS}

==========================
ALLOWED VALUES
==========================

status:
{", ".join(metadata["status"]["values"])}

priority:
{", ".join(metadata["priority"]["values"])}

category:
{", ".join(metadata["category"]["values"])}

agent_id:
{", ".join(metadata["agent_id"]["values"])}

==========================
IMPORTANT RULES
==========================

1. Generate ONLY SQLite SQL.
2. Return ONLY one SELECT statement.
3. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE, PRAGMA or ATTACH.
4. Use ONLY the allowed values exactly as listed above.
5. String comparisons are case-sensitive.
6. Never invent new category, priority or status values.
7. Never wrap SQL inside markdown.
8. Never explain the SQL.
9. Output ONLY the SQL statement.

==========================
SQL DIALECT
==========================

Use SQLite syntax only.

Supported Functions

- COUNT()
- AVG()
- SUM()
- MIN()
- MAX()
- ROUND()
- DATE()
- DATETIME()
- STRFTIME()

Do NOT use

- TOP
- ILIKE
- DATEDIFF
- DATEADD
- NOW()
- GETDATE()

Use LIMIT instead of TOP.
"""

def build_answer_prompt(question, sql, data, total_records):

    return f"""
You are an AI assistant that explains SQL query results to users.

The SQL query has already been executed successfully.

==========================
USER QUESTION
==========================

{question}

==========================
EXECUTED SQL
==========================

{sql}

==========================
TOTAL MATCHING RECORDS
==========================

{total_records}

==========================
DATABASE RESULT
==========================

{data}

==========================
INSTRUCTIONS
==========================

1. Answer ONLY using the database result.

2. Never make assumptions.

3. Never fabricate information.

4. Never mention SQL or databases.

5. If TOTAL MATCHING RECORDS is 0, reply exactly:
   "No matching records were found."

6. If the result is a single aggregated value (COUNT, AVG, SUM, MIN, MAX),
   answer naturally using that value.

Example:
"There are 121 open tickets."

Example:
"The average customer rating is 4.3."

7. If multiple records are returned:

   - First mention the total number of matching records.
   - Then provide a concise summary.
   - Mention important values such as Ticket ID, Agent ID, Status,
     Priority, Category or Rating when available.
   - Do not list more than the first 10 records.
   - If there are more than 10 records, mention:
     "Showing the first 10 records."

Example:

Found 8 matching tickets.

• Ticket ID: TKT-101 (High, Open)

• Ticket ID: TKT-145 (Critical, Escalated)

• Ticket ID: TKT-238 (High, Open)

Showing the first 10 records.

8. Keep the response concise and professional.

9. Never repeat the entire dataset.

10. Never invent Ticket IDs or values.
"""