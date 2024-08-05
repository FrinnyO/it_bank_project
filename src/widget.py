def mask_account_card(number: str) -> str:
    """Returns masked card or account number as string"""
    if 'Счет' in number:
        return f'{number[0:5]}{'*' * 2}{number[-4::]}'
    else:
        card_name = []
        for symbol in number:
            if symbol not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                card_name.append(symbol)
            else:
                break
        card_name_str = ''.join(card_name)
        return f'{card_name_str}{number[-16:-12]} {number[-12:-10]}{'*' * 2} {'*' * 4} {number[-4::]}'
