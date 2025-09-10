#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return list2
    list2[idx] = element
    return list2

    