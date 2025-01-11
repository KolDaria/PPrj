import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("value, expected", [
    ("Maestro 1596837868705199", "XXXX XX** **** XXXX"),
    ("Счет 64686473678894779589", "****************XXXX"),
    ("MasterCard 7158300734726758", "XXXX XX** **** XXXX"),
    ("Visa Classic 6831982476737658", "XXXX XX** **** XXXX"),
    ("Visa Platinum 8990922113665229", "XXXX XX** **** XXXX"),
    ("Visa Gold 5999414228426353", "XXXX XX** **** XXXX"),
    ("Bordo 1596837868705199", "Введены некорректные данные"),
    ("Число 41266666662335552", "Введены некорректные данные"),
    ("4533116132", "Введены некорректные данные"),
    ("jjkjhjhkk", "Введены некорректные данные"),
    ("", "Введены некорректные данные")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_mask_account_card_error():
    with pytest.raises(IndexError) as exc_info:
        mask_account_card("Visa 1254")
    assert str(exc_info.value) == "Номер карты должен быть равен 16 символам"
    with pytest.raises(IndexError) as exc_info:
        mask_account_card("Счет 16546")
    assert str(exc_info.value) == "Номер счета должен быть равен 20 символам"


@pytest.mark.parametrize("value, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-08-22T09:26:14.671407", "22.08.2023")
])
def test_get_date(value, expected):
    assert get_date(value) == expected


def test_get_date_error():
    with pytest.raises(IndexError) as exc_info:
        get_date("2023.08.22T09:26:14.671407")
    assert str(exc_info.value) == "list index out of range"
    with pytest.raises(IndexError) as exc_info:
        get_date("T09:26:14.671407")
    assert str(exc_info.value) == "list index out of range"
