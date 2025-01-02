from src.masks import get_mask_account, get_mask_card_number
import pytest


def test_get_mask_card_number(numbers):
    assert get_mask_card_number(numbers) == "XXXX XX** **** XXXX"
