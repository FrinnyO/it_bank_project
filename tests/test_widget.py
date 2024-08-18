import pytest

from src import masks, widget


@pytest.mark.parametrize(
    "number, mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361789", None),
        ("", None),
        ("Счет 73654108430135874305132", None),
    ],
)
def test_get_mask_card_number(number, mask):
    assert widget.mask_account_card(number) == mask


@pytest.mark.parametrize(
    "date, common_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-03-14T02:26:18.671407", "14.03.2022"),
        ("123", None),
        ("2024-03-11T02:26:18.671407484564132", None),
        ("", None),
        ("abc", None),
    ],
)
def test_get_date(date, common_date):
    assert widget.get_date(date) == common_date
