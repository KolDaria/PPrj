from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_CSV_XLSX import get_reading_financial_transactions_csv, get_reading_financial_transactions_xlsx
from src.search_description import get_transaction_data_from_the_search_bar
from src.utils import get_list_dict_transaction
from src.widget import get_date, mask_account_card

file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\operations.json'
path_cvs_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\transactions.csv'
path_xlsx_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\transactions_excel.xlsx'
python_transaction = get_list_dict_transaction(file)


def functionality_of_the_project():
    """
    Отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print('''Привет! Добро пожаловать в программу работы  с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла''')
    while True:
        try:
            number_input = int(input())
            if number_input in [1, 2, 3]:
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

    transactions = []
    file_type = ""

    if number_input == 1:
        print("Для обработки выбран JSON-файл")
        list_of_dicts = get_list_dict_transaction(file)
        file_type = "json"
    elif number_input == 2:
        print("Для обработки выбран CSV-файл")
        list_of_dicts = get_reading_financial_transactions_csv(path_cvs_file)
        file_type = "csv"
    elif number_input == 3:
        print("Для обработки выбран XLSX-файл")
        list_of_dicts = get_reading_financial_transactions_xlsx(path_xlsx_file)
        file_type = "xlsx"
    else:
        print("Введены не верные данные. Попробуйте еще раз")
        return None

    if not list_of_dicts:
        print("Не удалось загрузить данные. Проверьте файлы.")
        return

    while True:
        state = input('''Введите статус, по которому необходимо выполнить фильтрацию.
           Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ''').upper()
        if state in ("EXECUTED", "CANCELED", "PENDING"):
            print(f"Операции отфильтрованы по статусу \"{state}\"")
            break
        else:
            print(f"Статус операции \"{state}\" недоступен.")

    filter_list_dicts = filter_by_state(list_of_dicts, state)

    while True:
        sort_input = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if sort_input == "нет":
            transactions = filter_list_dicts
            break
        elif sort_input == "да":
            while True:
                sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower()
                if sort_order == "по возрастанию":
                    transactions = sort_by_date(filter_list_dicts, reverse=False)
                    break
                elif sort_order == "по убыванию":
                    transactions = sort_by_date(filter_list_dicts, reverse=True)
                    break
                else:
                    print("Не верно введены данные. Попробуйте еще раз.")
            break
        else:
            print("Не верно введены данные. Попробуйте еще раз.")

    while True:
        currency_input = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if currency_input == "да":
            list_dict_transactions = filter_by_currency(transactions, "RUB")
            break
        elif currency_input == "нет":
            list_dict_transactions = transactions
            break
        else:
            print("Не верно введены данные. Попробуйте еще раз")

    while True:
        filter_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
        if filter_choice == "да":
            substring = input("Введите ключевое слово для фильтрации: ").lower()
            filtered_transactions = get_transaction_data_from_the_search_bar(list_dict_transactions, substring)
            break
        elif filter_choice == "нет":
            filtered_transactions = list_dict_transactions
            break
        else:
            print("Не верно введены данные. Попробуйте еще раз")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for i, tx in enumerate(filtered_transactions):
        date = tx.get('date', 'Неизвестно')
        description = tx.get('description', 'Неизвестно')
        account_from = tx.get('from', 'Неизвестно')
        account_to = tx.get('to', 'Неизвестно')

        masked_from = mask_account_card(str(account_from)) if account_from else 'Неизвестно'
        masked_to = mask_account_card(str(account_to)) if account_to else 'Неизвестно'

        if file_type == "json":
            operation_amount = tx.get('operationAmount', {})
            amount = operation_amount.get('amount', 'Неизвестно')
            currency_data = operation_amount.get('currency', {})
            currency_name = currency_data.get('name', 'Неизвестно')
            currency_code = currency_data.get('code', 'Неизвестно')
        else:
            amount = tx.get('amount', 'Неизвестно')
            currency_name = tx.get('currency_name', 'Неизвестно')
            currency_code = tx.get('currency_code', 'Неизвестно')

        print(f"\n{get_date(date)} {description}")

        if "перевод" in description.lower() or "transfer" in description.lower():
            if masked_from != 'Неизвестно' and masked_to != 'Неизвестно':
                print(f"{masked_from} -> {masked_to}")
            elif account_from != 'Неизвестно' and account_to != 'Неизвестно':
                print(f"{account_from} -> {account_to}")

        if amount != 'Неизвестно':
            print(f"Сумма: {amount} {currency_name} ({currency_code})")
        else:
            print("Сумма: Неизвестно")
