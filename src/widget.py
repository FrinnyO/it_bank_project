from src import masks


def mask_account_card(number: str) -> str | None:
    """Returns masked card or account number as string"""
    if number.isalpha() or number.isdigit() or number.isspace() or number == "":
        return None
    if "Счет" in number:
        account_number = number[5:]
        if len(account_number) != 20:
            return None
        return f"{number[0:5]}{masks.get_mask_account(account_number)}"
    else:
        card_name = []
        for symbol in number:
            if symbol not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                card_name.append(symbol)
            else:
                symbol_index = number.index(symbol)
                number = number[symbol_index:]
                if len(number) != 16:
                    return None
                break
        card_name_str = "".join(card_name)
        return f"{card_name_str}{masks.get_mask_card_number(number)}"
    return None


def get_date(date: str) -> str | None:
    """Returns common date write as string"""
    if date.isdigit() or date.isspace() or date.isalpha() or date == "":
        return None
    if len(date) == 26:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return None
