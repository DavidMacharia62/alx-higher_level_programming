#!/usr/bin/python3
"""
Module 2-append_write

Appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the text file to append. (default: "")
        text (str): The string to append to the file. (default: "")

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, "a", encoding="utf-8") as file:
        count = file.write(text)
        return (count)
