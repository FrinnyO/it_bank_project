from operator import itemgetter


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Returns a list of dictionaries with a specific key"""
    list_of_dict_sorted = []
    for i in list_of_dict:
        if dict["state"] == state:
            list_of_dict_sorted.append(i)
    return list_of_dict_sorted


def sort_by_date(list_of_dict: list, sorter: bool = True) -> list:
    """Returns a list sorted by dates"""
    sorted_list = sorted(list_of_dict, key=itemgetter("date"), reverse=sorter)
    return sorted_list
