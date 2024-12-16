from src import processing


def test_filter_by_state_1(base_list_of_dict):
    assert processing.filter_by_state(base_list_of_dict, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_2(base_list_of_dict):
    assert processing.filter_by_state(base_list_of_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_3(base_list_of_dict):
    assert processing.filter_by_state(base_list_of_dict, "123") == []


def test_filter_by_state_4():
    assert processing.filter_by_state([]) == []


def test_sort_by_date_1(base_list_of_dict):
    assert processing.sort_by_date(base_list_of_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_2(two_similar_dates):
    assert processing.sort_by_date(two_similar_dates) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_sort_by_date_3(base_list_of_dict):
    assert processing.sort_by_date(base_list_of_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_4():
    assert processing.sort_by_date([]) == []


def test_get_transactions_by_description_not_found(base_list_of_transactions):
    assert processing.get_transactions_by_description(base_list_of_transactions, "Учеба") == []


def test_get_transactions_by_description_success(base_list_of_transactions):
    assert processing.get_transactions_by_description(base_list_of_transactions, "карт") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_count_operation_categories_not_found(base_list_of_transactions):
    assert processing.count_operation_categories(base_list_of_transactions, ["Оплата учебы", "Выплата кредита"]) == {}


def test_count_operation_categories_found(base_list_of_transactions):
    assert processing.count_operation_categories(
        base_list_of_transactions, ["Перевод организации", "Перевод со счета на счет"]
    ) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
    }
