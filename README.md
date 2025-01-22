# Проект "Виджет банковских операций клиента"

## **Описание:**

Проект "Виджет банковских операций клиента" - виджет, который показывает несколько последних успешных банковских операций клиента.
Проект был создан без импортируемых библиотек. 

## **Установка:**

Версия python для данного проекта `^3.13`

1. Установите Poetry:
```
curl -sSL https://install.python-poetry.org | python -
```
2. Клонируйте репозиторий:
```
git clone https://github.com/KolDaria/PPrj.git
```
3. Установите зависимости:
```
poetry add requests
```

## **Использование:**

### *Проект содержит:*

#### Папку `src` в которой реализованны следующее функции:

1. `__init__`: инициализация объекта.
2. `get_mask_card_number`: функция возвращает маску номера карты пользователя.
3. `get_mask_account`: функция возвращает маску номера счета пользователя.
4. `mask_account_card`: функция возвращает строку с замаскированным номером исходя из типа.
5. `get_date`: функция возвращает отформатированную строку с датой.
6. `filter_by_state`: функция возвращает новый список словарей исходя из заданного опционального значения.
7. `sort_by_date`: функция возвращает новый отсортированный список исходя из параметра задающего порядок сортировки.
8. `filter_by_currency`: функция возвращает итератор, который поочередно выдает транзакции.
9. `transaction_descriptions`: функция возвращает описание каждой операции по очереди из списка словарей с транзакциями.
10. `card_number_generator`: функция возвращает номера банковских карт из заданного 
начального и конечного значения для генерации диапазона номеров.
11. `log`: декоратор который автоматически логирует начало и конец выполнения функции, а также ее результаты 
или возникшие ошибки.
#### Папку `tests` в которой реализованно следующее:

1. `__init__`: инициализация объекта.
2. `test_masks.py`: модуль для тестирования функций `get_mask_account, get_mask_card_number`.
3. `test_widget.py`: модуль для тестирования функций `get_date, mask_account_card`.
4. `test_processing.py`: модуль для тестирования функций `filter_by_state, sort_by_date`.
5. `test_generators.py`: модуль для тестирования функций `filter_by_currency, transaction_descriptions, card_number_generator`
6. `test_decorators.py`: модуль для тестирования декоратора `log`.

##### Примеры использования функций `get_mask_account, get_mask_card_number`:

```python
from src.masks import get_mask_account, get_mask_card_number

# Пример для функции get_mask_card_number
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции

# Пример для функции get_mask_account
73654108430135874305  # входной аргумент
**4305  # выход функции
```

##### Примеры использования функций `get_date, mask_account_card`:

```python
from src.widget import get_date, mask_account_card

# Пример для карты в функции mask_account_card
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета в функции mask_account_card
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции

# Пример для функции get_date
"2024-03-11T02:26:18.671407" # входной аргумент
"ДД.ММ.ГГГГ"("11.03.2024") # выход функции
```

##### Примеры использования функций `filter_by_state, sort_by_date`:

```python
from src.processing import filter_by_state, sort_by_date

# Пример для функции filter_by_state
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Пример для функции sort_by_date
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

##### Примеры использования функций `filter_by_currency, transaction_descriptions, card_number_generator`:

```python
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Пример для функции filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }

# Пример для функции transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
    
# Пример для функции card_number_generator
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

##### Пример использования декоратора `log`:

```python
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

Ожидаемый вывод в лог-файл mylog.txt

при успешном выполнении:
my_function ok

Ожидаемый вывод при ошибке:
my_function error: тип ошибки. Inputs: (1, 2), {}

Где тип ошибки заменяется на текст ошибки.
```

## Тестирование функций:
```
---------- coverage: platform win32, python 3.13.0-final-0 -----------    
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\decorators.py             29      1    97%
src\generators.py             30      3    90%
src\masks.py                  19      0   100%
src\processing.py              8      0   100%
src\widget.py                 11      0   100%
tests\__init__.py              0      0   100%
tests\conftest.py              7      0   100%
tests\test_decorators.py      15      0   100%
tests\test_generators.py      31      0   100%
tests\test_masks.py           19      0   100%
tests\test_processing.py       8      0   100%
tests\test_widget.py          22      0   100%
----------------------------------------------
TOTAL                        199      4    98%
```
## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).