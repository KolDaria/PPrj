import re


def get_transaction_data_from_the_search_bar(list_dict_transactions: list[dict], substring: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    storage = []
    for objects in list_dict_transactions:
        description = objects.get('description', '')
        if description and re.search(substring, description, re.IGNORECASE):
            storage.append(objects)
    return storage
