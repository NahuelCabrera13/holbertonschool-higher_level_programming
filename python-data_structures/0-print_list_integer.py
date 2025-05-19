#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        if not isinstance(number, int):
            raise TypeError("All elements must be integers")
        print("{:d}" .format(number))
