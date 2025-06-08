#!/usr/bin/python3
"""Reads a CSV file and converts it to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): Name of the CSV input file.

    Returns:
        bool: True if conversion succeeds, False if file not found or error occurs.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
