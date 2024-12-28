def filter_by_state(list_of_dicts: list, state: str = 'EXECUTED') -> list:
    """
    Принимает список словарей и опционально значение для ключа и возвращает новый список словарей
    """
    new_lists = []
    for dicts in list_of_dicts:
        if dicts['state'] == state:
            new_lists.append(dicts)
    return new_lists


def sort_by_date(list_dicts_date: list, reverse: bool = True) -> list:
    """
    Принимает список словарей и параметр задающий порядок сортировки, возвращает новый отсортированный список
    """
    return sorted(list_dicts_date, key=lambda dicts_date: dicts_date['date'], reverse=reverse)
