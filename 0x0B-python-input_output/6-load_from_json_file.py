#!/usr/bin/python3
"""
Module 6-load_from_json_file

creates a Python obj from JSON file
"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
