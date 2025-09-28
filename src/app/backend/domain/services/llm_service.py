from abc import ABC, abstractmethod


class LLMService(ABC):
    @abstractmethod
    async def generate_answer(self, context: str, question: str) -> str:
        pass
