#!/usr/bin/python3
"""
Module 0-read_file

This is composed of the method read_file that reads into a file
and prints it's content into stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the text file to read. (default: "")

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist.

    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
