def get_mask_card_number(number_card: [int, str]) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    """
    number_card = str(number_card)
    mask_card_number = []
    for i in range(0, len(number_card), 4):
        result = number_card[i:i + 4]
        mask_card_number.append(result)
        if len(number_card) != 16:
            raise IndexError("Номер карты должен быть равен 16 символам")
    mask_card_number[0], mask_card_number[3] = "XXXX", "XXXX"
    mask_card_number[1], mask_card_number[2] = "XX**", "****"
    return " ".join(mask_card_number)


def get_mask_account(account_number: [int, str]) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    """
    account_number = str(account_number)
    mask_account = ("*" * len(account_number[:-4])) + ("X" * len(account_number[-4:]))
    if account_number.isalpha() or account_number == " ":
        return "Введены некорректные данные"
    elif len(account_number) != 20:
        raise IndexError("Номер счета должен быть равен 20 символам")
    return mask_account
