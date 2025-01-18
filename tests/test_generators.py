import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_result", [
    ("USD", 3),
    ("RUB", 2),
    ("EUR", 0)
])
def test_filter_by_currency(transactions, currency, expected_result):
    usd_transactions = list(filter_by_currency(transactions, currency))
    assert len(usd_transactions) == expected_result


def test_filter_by_currency_error_type(transactions):
    with pytest.raises(TypeError):
        filter_by_currency([])


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == 'Перевод организации'
    assert next(descriptions) == 'Перевод со счета на счет'
    assert next(descriptions) == 'Перевод со счета на счет'
    assert next(descriptions) == 'Перевод с карты на карту'
    assert next(descriptions) == 'Перевод организации'


def test_transaction_descriptions_error_iteration(transactions):
    transactions = [{}]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) is None
    with pytest.raises(StopIteration):
        next(descriptions)


@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, '0000 0000 0000 0001'),
    (9999999999999998, 9999999999999999, '9999 9999 9999 9998')])
def test_card_number_generator(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert next(generator) == expected


def test_card_number_generator_error_type():
    start, stop = "n", "k"
    generator = card_number_generator(start, stop)
    with pytest.raises(TypeError):
        next(generator)
