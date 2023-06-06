#!/usr/bin/python3
"""
This is a Locked class
"""


class LockedClass:
    """
    Prevents user from creating a new instace
    dynamically
    """

    __slots__ = "first_name"
