import json
import requests
from dotenv import load_dotenv
from .get_token import get_access_token
from ....utils.prompt_templates import get_system_prompt
import logging

logger = logging.getLogger(__name__)

def call_ai_model(prompt: str) -> str:
    """
    Конечная обработка текста с помощью GPT.

    Args:
        :param text: Исходный текст
        :type text: str
        :return: Dict с данными, полученными из текста
        :rtype: dict or None
        prompt:
    """
    logger.debug(f"Calling AI model with prompt: {prompt[:100]}...")
    url: str = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    load_dotenv()
    access_token: str = get_access_token()
    sys_prompt: str = get_system_prompt()
    # Параметры запроса
    payload = json.dumps(
        {
            "model": "GigaChat Lite",
            "messages": [{"role": "user", "content": prompt}, {"role": "system", "content": sys_prompt}],
            "stream": False,
            "repetition_penalty": 1,
        }
    )

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    # Получение ответа и статус кода
    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
    )

    status_code: int = response.status_code
    if status_code == 401:
        api_token: str = get_access_token()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_token}",
        }
        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )
        response_json = json.loads(response.text)
        content = response_json["choices"][0]["message"]["content"]
        logger.debug(f"AI model response received: {content[:100]}...")
        return content
    elif status_code == 200:
        response_json = json.loads(response.text)
        content = response_json["choices"][0]["message"]["content"]
        logger.debug(f"AI model response received: {content[:100]}...")
        return content
    else:
        logger.error(f"Unexpected status code: {status_code}")
        raise Exception(f"Unexpected status code: {status_code}")