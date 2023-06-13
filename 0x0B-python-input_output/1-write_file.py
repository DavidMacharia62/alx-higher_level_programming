#!/usr/bin/python3
"""
Module 1-write_file.py

This is composed of the method 1-write_file that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the text file to write. (default: "")
        text (str): The string to write to the file. (default: "")

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, "w", encoding="utf-8") as file:
        count = file.write(text)
        return count
