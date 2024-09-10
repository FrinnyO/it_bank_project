from unittest.mock import Mock, patch

from src import external_api


def test_convert_into_rubs_1():
    assert (
        external_api.convert_into_rubs(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )


def test_convert_into_rubs_2(usd_transaction, result):
    mock_get = Mock()
    mock_get.status_code = 200
    mock_get.json.return_value = result
    with patch("requests.get", return_value=mock_get):
        result = external_api.convert_into_rubs(usd_transaction)
        assert result == 256325.23


def test_convert_into_rubs_3():
    assert external_api.convert_into_rubs({}) == False
