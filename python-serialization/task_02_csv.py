#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to a JSON file.

    Parameters:
        filename (str): The name of the input CSV file.

    Returns:
        bool: True if was successful, False otherwise.
    """
    try:
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))

        return True

    except FileNotFoundError as e:
        print(e)
        return False

    except Exception as e:
        print(e)
        return False
