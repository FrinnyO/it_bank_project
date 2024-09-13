import json
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/application.log",
    filemode="w",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)
logger.info("Запуск модуля")


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
