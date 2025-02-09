import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7452365874568521) == "XXXX XX** **** XXXX"


def test_get_mask_card_number_error():
    with pytest.raises(IndexError) as exc_info:
        get_mask_card_number(125487)
    with pytest.raises(IndexError) as exc_info:
        get_mask_card_number(12548741223132255)
    with pytest.raises(IndexError) as exc_info:
        get_mask_card_number(" ")
    assert str(exc_info.value) == "Номер карты должен быть равен 16 символам"


@pytest.mark.parametrize("value, expected", [
    (15328974562158744568, "****************XXXX"),
    (" ", "Введены некорректные данные: номер счета должен содержать только цифры"),
    ("jljlkhkjgglhgdgh", "Введены некорректные данные: номер счета должен содержать только цифры")
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_error():
    assert get_mask_account(456897215) == "Номер счета должен быть равен 20 символам"
