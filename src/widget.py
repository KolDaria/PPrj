from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером
    """
    if "Счет" in string:
        return get_mask_account(string[-20:])
    elif "Visa" in string or "MasterCard" in string or "Maestro" in string:
        return get_mask_card_number(string[-16:])
    else:
        return "Введены некорректные данные"


def get_date(string_date: str) -> str:
    """
    Принимает на вход строку с датой и возвращает отформатированную строку с датой
    """
    slice_date = string_date[0:10].split("-")
    slice_date[0], slice_date[2] = slice_date[2], slice_date[0]
    return ".".join(slice_date)
