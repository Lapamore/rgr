from fastapi import APIRouter, HTTPException
from ....models.request_models import SummaryRequest, SummaryResponse
from ....services.summarizer import summarizer
from .ai_integration import call_ai_model
router = APIRouter()
import logging

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание обработчика для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Форматирование логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(console_handler)

@router.post("/summary", response_model=SummaryResponse)
async def create_summary(request: SummaryRequest) -> SummaryResponse:
    """
    Create a summary of the provided text.
    
    Args:
        request: SummaryRequest object containing text
        
    Returns:
        SummaryResponse: Contains the generated summary
        
    Raises:
        HTTPException: If summarization fails
    """
    try:
        result = await summarizer.summarize(text=request.text)
        # result: dict =  {
        #     "summary": call_ai_model(prompt=request.text)
        # }
        return SummaryResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate summary: {str(e)}"
        )