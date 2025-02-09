from collections import Counter


def get_dict_of_transactions_depending_category(list_transactions: list[dict], list_category: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    storage = []
    for transaction in list_transactions:
        if transaction['description'] in list_category:
            storage.append(transaction['description'])
    counted = Counter(storage)
    return dict(counted)
