#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    new_str = ''
    for character in str:
        character_code = ord(character)
        if character_code in range(97, 123):
            character_code -= 32
        new_str += chr(character_code)
    print("{:s}".format(new_str))
