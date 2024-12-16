import re
from collections import Counter
from operator import itemgetter
from typing import List


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list | None:
    """Returns a list of dictionaries with a specific key"""
    if list_of_dict == []:
        return []
    list_of_dict_sorted = []
    for i in list_of_dict:
        if i["state"] == state:
            list_of_dict_sorted.append(i)
    return list_of_dict_sorted


def sort_by_date(list_of_dict: list, sorter: bool = True) -> list | None:
    """Returns a list sorted by dates"""
    if list_of_dict == []:
        return []
    sorted_list = sorted(list_of_dict, key=itemgetter("date"), reverse=sorter)
    return sorted_list


def get_transactions_by_description(transactions: List[dict], search_string: str) -> List[dict]:
    """Функция принимает список транзакций и возвращает транзакции
    соответствующие строке поиска по описанию транзакции"""
    pattern = rf"{search_string}"
    return [trans for trans in transactions if re.search(pattern, trans["description"], flags=re.IGNORECASE)]


def count_operation_categories(transactions: List[dict], categories_list: list) -> dict:
    """Функция считает количество операций по каждой категории из заданного списка"""
    return dict(Counter([x["description"] for x in transactions if x["description"] in categories_list]))
