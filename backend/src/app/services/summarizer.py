import ollama
from ..core.config import get_settings
from ..utils.prompt_templates import get_system_prompt

settings = get_settings()

class SummarizerService:
    def __init__(self):
        self.model_name = settings.MODEL_NAME

    async def summarize(self, text: str) -> dict:
        """
        Обобщите данный текст, используя модель LLM.
        
        Args:
            text: Введенное сообщение для обобщения
            
        Returns:
            dict: Содержит краткий текст
        """
        system_prompt = get_system_prompt()
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Вот текст для суммаризации:\n{text}"}
                ]
            )
            
            return {
                "summary": response["message"]["content"]
            }
            
        except Exception as e:
            raise Exception(f"Ошибка при суммаризации текста: {str(e)}")


# Singleton instance
summarizer = SummarizerService()
