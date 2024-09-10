import json
from unittest.mock import Mock

from src import utils


def test_get_transactions_and_descriptions_1():
    mock_json_obj = Mock(return_value=[{"id": 456852, "state": "EXECUTED"}])
    json.load = mock_json_obj
    assert utils.get_transactions_and_descriptions() == [{"id": 456852, "state": "EXECUTED"}]
    mock_json_obj.assert_called()


def test_get_transactions_and_descriptions_2():
    mock_json_obj = Mock(return_value=[])
    json.load = mock_json_obj
    assert utils.get_transactions_and_descriptions() == []
    mock_json_obj.assert_called()


def test_get_transactions_and_descriptions_3():
    assert utils.get_transactions_and_descriptions("a") == []
