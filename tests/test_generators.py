import pytest

from src import generators


def test_filter_by_currency(base_list_of_transactions):
    generator = generators.filter_by_currency(base_list_of_transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_1(base_list_of_transactions):
    generator = generators.filter_by_currency(base_list_of_transactions, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_transaction_descriptions(base_list_of_transactions):
    generator = generators.transaction_descriptions(base_list_of_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    with pytest.raises(StopIteration):
        assert next(generator)


def test_transaction_descriptions_1():
    generator = generators.transaction_descriptions([])
    with pytest.raises(StopIteration):
        assert next(generator)


def test_card_number_generator_1():
    generator = generators.card_number_generator(100, 105)
    assert next(generator) == "0000 0000 0000 0100"
    assert next(generator) == "0000 0000 0000 0101"
    assert next(generator) == "0000 0000 0000 0102"
    assert next(generator) == "0000 0000 0000 0103"
    assert next(generator) == "0000 0000 0000 0104"
    assert next(generator) == "0000 0000 0000 0105"


@pytest.mark.parametrize("start, stop", [(-100, 100), (1, 10000000000000000), (100, 1)])
def test_card_number_generator_2(start, stop):
    with pytest.raises(ValueError):
        assert next(generators.card_number_generator(start, stop))
