import csv

import pandas as pd


def get_reading_financial_transactions_csv(path_cvs_file: str) -> list[dict]:
    """
    Считывание финансовых операций из CSV-файлов.
    """
    try:
        with open(path_cvs_file, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
        return list(reader)
    except FileNotFoundError:
        return []


path_cvs_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\transactions.csv'


def get_reading_financial_transactions_xlsx(path_xlsx_file: str) -> list[dict]:
    """
    Считывание финансовых операций из XLSX-файлов.
    """
    try:
        list_row = []
        excel_data = pd.read_excel(path_xlsx_file)
        for index, row in excel_data.iterrows():
            list_row.append(dict(row))
        return list_row
    except FileNotFoundError:
        return []


path_xlsx_file = 'C:\\Users\\Dr\\Desktop\\PPrj\\data\\transactions_excel.xlsx'
