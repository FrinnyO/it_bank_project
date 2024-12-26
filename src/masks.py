import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
    """Returns masked card number as string"""
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Успешная маскировка номера карты")
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    else:
        logger.warning("Неудачная попытка маскировки номера карты")
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Returns masked account number as string"""
    if acc_number.isdigit() and len(acc_number) == 20:
        logger.info("Успешная маскировка номера счета")
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        logger.warning("Неудачная попытка маскировки номера счета")
        return None
