#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    (number, "is zero")

elif number > 0:
    (number, "is positive")

else:
    (number, "is negative")
