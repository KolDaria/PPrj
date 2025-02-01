import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def get_a_transaction_conversion(python_transaction: Any) -> Any:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях
    """
    for transact in python_transaction:
        if transact["operationAmount"]["currency"]["code"] != "RUB":
            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {
                "amount": transact["operationAmount"]["amount"],
                "from": transact["operationAmount"]["currency"]["code"],
                "to": "RUB"
            }
            headers = {
                "apikey": f"{api_key}"
            }

            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            result = response.json()
            if status_code == 200:
                return round(float(result["result"]), 2)
            else:
                return f"Ошибка запроса. Причина: {response.reason}"
        else:
            return round(float(transact["operationAmount"]["amount"]), 2)
