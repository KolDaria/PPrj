import json
import logging
import os
from typing import Any

logs_dir = '../logs'
os.makedirs(logs_dir, exist_ok=True)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(os.path.join(logs_dir, 'utils.log'), mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_list_dict_transaction(file_json: Any) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    """
    logger.info('Запуск....')
    try:
        with open(file_json, encoding='utf-8') as file_json:
            data_json = json.load(file_json)
            logger.info('Конвертация json - файла в python - объект прошла успешно')
            return data_json
    except json.JSONDecodeError:
        logger.error('Ошибка, json - файл пуст')
        return list()
    except FileNotFoundError:
        logger.error('Ошибка, json - файл не найден')
        return list()


file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\operations.json'
