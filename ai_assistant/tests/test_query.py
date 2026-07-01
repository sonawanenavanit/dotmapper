from services.query_service import QueryService

query = QueryService()

response = query.execute(

    "How many tickets are open?"

)

print(response)