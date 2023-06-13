#!/usr/bin/python3
"""
Module 5-save_from_json_file.py

writes Python obj to file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON representation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
