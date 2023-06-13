#!/usr/bin/python3
"""
Module 3_from_json_string

returns python data structure from JSON string
"""


def from_json_string(my_string):
    """Returns python data structure from JSON string

    Args:
        my_str: json string representation
    Return:
        python object
    """
    import json

    return json.loads(my_string)
