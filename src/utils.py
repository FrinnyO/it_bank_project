import json
import os


def get_transactions_and_descriptions(file_name="operations.json") -> dict:
    """Функция передаёт операции и их описание из json файла"""
    try:
        with open(f"D:/it_bank_project/data/{file_name}", encoding="utf-8") as f:
            if os.stat(f"D:/it_bank_project/data/{file_name}").st_size == 0:
                return []
            else:
                operations = json.load(f)
        return operations
    except FileNotFoundError:
        return []
