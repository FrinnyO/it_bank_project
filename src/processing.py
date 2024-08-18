from operator import itemgetter


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
