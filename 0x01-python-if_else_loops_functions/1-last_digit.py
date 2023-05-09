#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    divisor = 10
else:
    divisor = -10
if (number % divisor) > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, number % divisor))
elif (number % divisor) == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, number % divisor))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, number % divisor))
