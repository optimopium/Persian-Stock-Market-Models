import os
import csv
from django.conf import settings


def load_symbols_from_csv(columns=None, path=None):
    columns = columns or ['symbol']
    # Use BASE_DIR from settings to construct the path to the CSV file
    if path:
        csv_file_path = path
    else:
        csv_file_path = os.path.join(settings.BASE_DIR, 'data/files/symbols.csv')

    symbols = []

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                selected_columns = {col: row[col] for col in columns if col in row}
                symbols.append(selected_columns)
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e

    return symbols
