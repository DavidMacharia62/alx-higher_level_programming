#!/usr/bin/python3
for num in range(122, 96, -1):
    offset = 32
    if num % 2 == 0:
        offset = 0
    print("{}".format(chr(num - offset)), end="")
