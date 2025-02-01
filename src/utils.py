import json
from typing import Any


def get_list_dict_transaction(file_json: Any) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(file_json, encoding='utf-8') as file_json:
            data_json = json.load(file_json)
            return data_json
    except json.JSONDecodeError:
        return list()
    except FileNotFoundError:
        return list()


file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\operations.json'


python_transaction = get_list_dict_transaction(file)
