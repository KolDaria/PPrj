import json
from unittest.mock import mock_open, patch

from src.utils import get_list_dict_transaction


def test_get_list_dict_transaction_json_file():
    json_file = '[{"id": 441945886, "state": "EXECUTED"}]'
    with patch('builtins.open', mock_open(read_data=json_file)):
        result = get_list_dict_transaction('mock_file.json')
        assert result == json.loads(json_file)


def test_get_list_dict_transaction_empty_file():
    json_content = ''
    with patch('builtins.open', mock_open(read_data=json_content)):
        result = get_list_dict_transaction('mock_file.json')
        assert result == []


def test_get_list_dict_transaction_invalid_json_file():
    json_content = 'invalid_json'
    with patch('builtins.open', mock_open(read_data=json_content)):
        result = get_list_dict_transaction('mock_file.json')
        assert result == []


def test_get_list_dict_transaction_file_not_found():
    result = get_list_dict_transaction('non_existent_file.json')
    assert result == []
