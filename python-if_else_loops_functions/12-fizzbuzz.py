#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            s = "FizzBuzz"
        elif i % 3 == 0:
            s = "Fizz"
        elif i % 5 == 0:
            s = "Buzz"
        else:
            s = str(i)
        print(s, end=" ")
