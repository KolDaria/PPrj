from unittest.mock import patch

from main import functionality_of_the_project


@patch('main.get_list_dict_transaction')
@patch('main.get_reading_financial_transactions_csv')
@patch('main.get_reading_financial_transactions_xlsx')
def test_functionality_of_the_project_json(mock_xlsx, mock_csv, mock_json, capsys):
    mock_json.return_value = [{"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00",
                               "description": "Test transaction"}]
    with patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет', 'нет', 'нет']):
        functionality_of_the_project()
    captured = capsys.readouterr()
    assert "Для обработки выбран JSON-файл" in captured.out
    assert "Всего банковских операций в выборке: 1" in captured.out


@patch('main.get_list_dict_transaction')
@patch('main.get_reading_financial_transactions_csv')
@patch('main.get_reading_financial_transactions_xlsx')
def test_functionality_of_the_project_csv(mock_xlsx, mock_csv, mock_json, capsys):
    mock_csv.return_value = [{"id": 2, "state": "EXECUTED", "date": "2023-01-02T00:00:00",
                              "description": "Test transaction"}]
    with patch('builtins.input', side_effect=['2', 'EXECUTED', 'нет', 'нет', 'нет']):
        functionality_of_the_project()
    captured = capsys.readouterr()
    assert "Для обработки выбран CSV-файл" in captured.out
    assert "Всего банковских операций в выборке: 1" in captured.out


@patch('main.get_list_dict_transaction')
@patch('main.get_reading_financial_transactions_csv')
@patch('main.get_reading_financial_transactions_xlsx')
def test_functionality_of_the_project_xlsx(mock_xlsx, mock_csv, mock_json, capsys):
    mock_xlsx.return_value = [{"id": 3, "state": "EXECUTED", "date": "2023-01-03T00:00:00",
                               "description": "Test transaction"}]
    with patch('builtins.input', side_effect=['3', 'EXECUTED', 'нет', 'нет', 'нет']):
        functionality_of_the_project()
    captured = capsys.readouterr()
    assert "Для обработки выбран XLSX-файл" in captured.out
    assert "Всего банковских операций в выборке: 1" in captured.out


@patch('main.get_list_dict_transaction')
@patch('main.get_reading_financial_transactions_csv')
@patch('main.get_reading_financial_transactions_xlsx')
def test_functionality_of_the_project_invalid_status(mock_xlsx, mock_csv, mock_json, capsys):
    mock_json.return_value = [{"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00",
                               "description": "Test transaction"}]
    with patch('builtins.input', side_effect=['1', 'INVALID', 'EXECUTED', 'нет', 'нет', 'нет']):
        functionality_of_the_project()
    captured = capsys.readouterr()
    assert "Статус операции \"INVALID\" недоступен." in captured.out
    assert "Всего банковских операций в выборке:" in captured.out
