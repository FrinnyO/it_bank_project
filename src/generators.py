from typing import Generator, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает транзакции отфильтрованные по заданной валюте в виде словаря"""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list) -> Iterator:
    """Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    return map(lambda x: x["description"], transactions)


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты."""
    over_max_number = 10000000000000000
    if 0 < start < stop < over_max_number:
        for i in range(start, stop + 1):
            new_number = over_max_number + i
            card_number = str(new_number)
            yield f"{card_number[1:5]} {card_number[5:9]} {card_number[9:13]} {card_number[13:]}"
    else:
        raise ValueError("Проверьте корректность введенного диапазона")
