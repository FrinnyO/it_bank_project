import json
import logging
import os

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)



def get_transactions_and_descriptions(file_name="operations.json") -> dict:
    """Функция передаёт операции и их описание из json файла"""
    try:
        with open(f"D:/it_bank_project/data/{file_name}", encoding="utf-8") as f:
            if os.stat(f"D:/it_bank_project/data/{file_name}").st_size == 0:
                logger.warning("Операций нет")
                return []
            else:
                operations = json.load(f)
                logger.info("Успешная запись операций")
        return operations
    except FileNotFoundError or json.JSONDecodeError:
        logger.warning("Файл не найден")
        return []
