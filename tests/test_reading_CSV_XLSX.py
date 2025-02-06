from unittest.mock import mock_open, patch

import pandas as pd

from src.reading_CSV_XLSX import (get_reading_financial_transactions_csv, get_reading_financial_transactions_xlsx,
                                  path_cvs_file, path_xlsx_file)


def test_get_reading_financial_transactions_csv():
    with patch('builtins.open', mock_open(read_data='')) as mock_file:
        with patch('csv.DictReader') as mock_get:
            mock_get.return_value = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                      'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
                                      'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                      'description': 'Перевод организации'}]
            assert get_reading_financial_transactions_csv(path_cvs_file) == [{'id': '650703', 'state': 'EXECUTED',
                                                                              'date': '2023-09-05T11:30:32Z',
                                                                              'amount': '16210',
                                                                              'currency_name': 'Sol',
                                                                              'currency_code': 'PEN',
                                                                              'from': 'Счет 58803664561298323391',
                                                                              'to': 'Счет 39745660563456619397',
                                                                              'description': 'Перевод организации'}]
            mock_get.assert_called_once_with(mock_file.return_value, delimiter=';')


def test_get_reading_financial_transactions_csv_empty_file():
    with patch('builtins.open', mock_open(read_data='')) as mock_file:
        with patch('csv.DictReader') as mock_get:
            mock_get.return_value = ''
            assert get_reading_financial_transactions_csv(path_cvs_file) == []
            mock_get.assert_called_once_with(mock_file.return_value, delimiter=';')


def test_get_reading_financial_transactions_csv_file_not_found():
    path_cvs_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\non_existent_file.csv'
    assert get_reading_financial_transactions_csv(path_cvs_file) == []


def test_get_reading_financial_transactions_xlsx():
    with patch('pandas.read_excel') as mock_get:
        mock_get.return_value = pd.DataFrame([{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                               'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN',
                                               'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                               'description': 'Перевод организации'}])
        assert get_reading_financial_transactions_xlsx(path_xlsx_file) == [{'id': '650703', 'state': 'EXECUTED',
                                                                            'date': '2023-09-05T11:30:32Z',
                                                                            'amount': '16210', 'currency_name': 'Sol',
                                                                            'currency_code': 'PEN',
                                                                            'from': 'Счет 58803664561298323391',
                                                                            'to': 'Счет 39745660563456619397',
                                                                            'description': 'Перевод организации'}]
        mock_get.assert_called_once_with(path_xlsx_file)


def test_get_reading_financial_transactions_xlsx_empty_file():
    with patch('pandas.read_excel') as mock_get:
        mock_get.return_value = pd.DataFrame()
        assert get_reading_financial_transactions_xlsx(path_xlsx_file) == []
        mock_get.assert_called_once_with(path_xlsx_file)


def test_get_reading_financial_transactions_xlsx_file_not_found():
    path_xlsx_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\non_existent_file.xlsx'
    assert get_reading_financial_transactions_xlsx(path_xlsx_file) == []
