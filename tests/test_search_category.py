import pytest

from src.search_category import get_dict_of_transactions_depending_category


@pytest.mark.parametrize("transactions, category, expected", [
    ([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
       'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
       'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
       'description': 'Перевод организации'}], ["Перевод с карты на карту", "Перевод со счета на счет",
                                                "Перевод организации", "Открытие вклада"],
     {"Перевод организации": 1}),
    ([], ["Перевод с карты на карту", "Перевод со счета на счет", "Перевод организации", "Открытие вклада"], {}),
    ([], [], {}),
    ([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
       'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
       'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
       'description': 'Перевод организации'}], ["Зерно"], {})
])
def test_get_dict_of_transactions_depending_category(transactions, category, expected):
    assert get_dict_of_transactions_depending_category(transactions, category) == expected
