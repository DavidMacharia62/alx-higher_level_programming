#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            # convert lowercase character to uppercase using ASCII values
            upper_c = chr(ord(c) - 32)
        else:
            # leave character unchanged if not lowercase
            upper_c = c
        print("{}".format(upper_c), end="")
    print()  # print newline after loop
