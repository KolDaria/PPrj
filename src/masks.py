import logging
import os.path

logs_dir = '../logs'
os.makedirs(logs_dir, exist_ok=True)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(os.path.join(logs_dir, 'masks.log'), mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: [int, str]) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    """
    logger.info('Запуск функции маскировки номера карты')
    number_card = str(number_card)
    mask_card_number = []
    for i in range(0, len(number_card), 4):
        result = number_card[i:i + 4]
        mask_card_number.append(result)
        if len(number_card) != 16:
            logger.error('Ошибка, номер карты не равен 16 символам')
            raise IndexError("Номер карты должен быть равен 16 символам")
    mask_card_number[0], mask_card_number[3] = "XXXX", "XXXX"
    mask_card_number[1], mask_card_number[2] = "XX**", "****"
    logger.info('Маскировка номера карты прошла успешно')
    return " ".join(mask_card_number)


def get_mask_account(account_number: [int, str]) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    """
    logger.info('Запуск функции маскировки номера счета')
    account_number = str(account_number)
    mask_account = ("*" * len(account_number[:-4])) + ("X" * len(account_number[-4:]))
    if account_number.isalpha() or account_number == " ":
        logger.warning('Введены некорректные данные')
        return "Введены некорректные данные"
    elif len(account_number) != 20:
        logger.error('Ошибка, номер счета не равен 20 символам')
        raise IndexError("Номер счета должен быть равен 20 символам")
    logger.info('Маскировка номера счета прошла успешно')
    return mask_account
