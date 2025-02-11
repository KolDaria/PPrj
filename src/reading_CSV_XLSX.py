import csv

import pandas as pd


def get_reading_financial_transactions_csv(path_cvs_file: str) -> list[dict]:
    """
    Считывание финансовых операций из CSV-файлов.
    """
    try:
        transactions = []
        with open(path_cvs_file, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if any(row.values()):
                    transactions.append(row)
            return transactions
    except FileNotFoundError:
        return []


path_cvs_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\transactions.csv'


def get_reading_financial_transactions_xlsx(path_xlsx_file: str) -> list[dict]:
    """
    Считывание финансовых операций из XLSX-файлов.
    """
    try:
        excel_data = pd.read_excel(path_xlsx_file)
        transactions = []
        for index, row in excel_data.iterrows():
            if not row.isnull().all():
                transactions.append(dict(row))
        return transactions
    except FileNotFoundError:
        return []


path_xlsx_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\transactions_excel.xlsx'
