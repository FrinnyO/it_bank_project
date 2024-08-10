import widget


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Returns a list of dictionaries with a specific key"""
    list_of_dict_sorted = []
    for dict in list_of_dict:
        if dict["state"] == state:
            list_of_dict_sorted.append(dict)
    return list_of_dict_sorted


def sort_dates(dates_list: list) -> tuple:
    """Returns splited write of dates"""
    split_up = dates_list.split(".")
    return split_up[2], split_up[1], split_up[0]


def sort_by_date(list_of_dict: list, sorter: bool = True) -> list:
    """Returns a list sorted by dates"""
    list_of_dates_old = []
    list_of_dates_new = []
    list_of_dict_sorted = []
    for dict in list_of_dict:
        list_of_dates_old.append(dict["date"])
    for date in list_of_dates_old:
        list_of_dates_new.append(widget.get_date(date))
    list_of_dates_new.sort(key = sort_dates, reverse = sorter)
    for date in list_of_dates_new:
        for dict in list_of_dict:
            if widget.get_date(dict["date"]) == date:
                list_of_dict_sorted.append(dict)
    return list_of_dict_sorted
