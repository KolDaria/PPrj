import pytest

from src.search_description import get_transaction_data_from_the_search_bar


@pytest.mark.parametrize("transactions, string, expected", [
    ([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
       'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
       'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
       'description': 'Перевод организации'}], "Перевод", [{'id': '650703', 'state': 'EXECUTED',
                                                            'date': '2023-09-05T11:30:32Z',
                                                            'amount': '16210', 'currency_name': 'Sol',
                                                            'currency_code': 'PEN',
                                                            'from': 'Счет 58803664561298323391',
                                                            'to': 'Счет 39745660563456619397',
                                                            'description': 'Перевод организации'}]),
    ([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
       'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
       'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
       'description': 'Перевод организации'}], "Оплата", []),
    ([], "", [])
])
def test_get_transaction_data_from_the_search_bar(transactions, string, expected):
    assert get_transaction_data_from_the_search_bar(transactions, string) == expected
