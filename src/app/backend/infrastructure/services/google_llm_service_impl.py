from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from app.backend.domain.services.llm_service import LLMService

class GoogleLLMServiceImpl(LLMService):
    def __init__(self, api_key: str, model: str):
        self.llm = ChatGoogleGenerativeAI(model=model, api_key=api_key)

        template = """Usa únicamente el contexto proporcionado para responder la pregunta final.
        Si no sabes la respuesta, di que no sabes, no intentes inventar una respuesta.
        Usa máximo tres oraciones y mantén la respuesta lo más concisa posible.
        Siempre di "¡gracias por preguntar!" al final de la respuesta.

        {context}

        Pregunta: {question}

        Respuesta útil:"""

        self.prompt = PromptTemplate.from_template(template)

    async def generate_answer(self, context: str, question: str) -> str:
        chain = self.prompt | self.llm

        response = chain.invoke({"context": context, "question": question})
        return response.content
