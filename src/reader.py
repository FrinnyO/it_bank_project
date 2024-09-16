import pandas as pd


def csv_reader(way_to_file: str) -> list | str:
    """Функция считывающая список транзакций из src файла"""
    try:
        csv_transactions = pd.read_csv(way_to_file)
    except FileNotFoundError:
        return "Файл не найден"
    else:
        return csv_transactions.to_dict(orient="records")


def excel_reader(way_to_file: str) -> list | str:
    """Функция считывающая список транзакций из excel файла"""
    try:
        excel_transactions = pd.read_excel(way_to_file)
    except FileNotFoundError:
        return "Файл не найден"
    else:
        return excel_transactions.to_dict(orient="records")
