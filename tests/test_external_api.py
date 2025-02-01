import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from external_api import get_a_transaction_conversion

load_dotenv()
api_key = os.getenv('API_KEY')


@pytest.mark.parametrize("status_code, result", [
    (200, {"result": 3724.305775, "success": "true"}),
    (400, None)
])
@patch('requests.get')
def test_get_a_transaction_conversion(mock_get, status_code, result):
    python_transaction = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
      }
    ]

    mock_response = Mock()
    mock_response.status_code = status_code
    mock_response.json.return_value = result
    mock_get.return_value = mock_response

    get_a_transaction_conversion(python_transaction)

    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert',
                                     headers={'apikey': f"{api_key}"},
                                     params={'amount': '31957.58', 'from': 'USD', 'to': 'RUB'})
