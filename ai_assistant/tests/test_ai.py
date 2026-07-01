from services.ai_service import AIService

llm = AIService().get_llm()

response = llm.invoke("Say Hello")

print(response.content)