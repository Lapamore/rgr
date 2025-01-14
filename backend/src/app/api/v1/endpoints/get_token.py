import requests
import json


def get_access_token() -> str:
    '''
    Получение токенка доступа.
    '''
    url: str = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    auth_key: str = "YzdhMzIzODItOTE0ZS00YmVlLWFkOGMtZTRjOWIzYjIwYzBjOmYwZDVlNWMxLTNhMGYtNDQ3NS04OGRjLTdlZWM2ZTQxYzcwZg=="
    
    payload: dict ={
        'scope': 'GIGACHAT_API_PERS'
    }
    headers: dict = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': '3920861a-a708-42e4-a6e7-8580bfa35e84',
        'Authorization': f'Basic {auth_key}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    status_code: int = response.status_code
    if status_code == 200:
        response_text: str  = response.text
        response_json: dict = json.loads(response_text)
        access_token: str = response_json["access_token"]
        return access_token

if __name__ == "__main__":
    get_access_token()