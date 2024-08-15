import pytest
from src import masks


@pytest.mark.parametrize('card_number, mask', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('1256384596425836', '1256 38** **** 5836'),
    ('1325459451345964543', None),
    ('', None),
])
def test_get_mask_card_number(card_number, mask):
    assert masks.get_mask_card_number(card_number) == mask

@pytest.mark.parametrize('acc_number, mask', [
    ('73654108430135874305', '**4305'),
    ('15654815484654899994231', None),
    ('', None)
])
def test_get_mask_account(acc_number, mask):
    assert masks.get_mask_account(acc_number) == mask