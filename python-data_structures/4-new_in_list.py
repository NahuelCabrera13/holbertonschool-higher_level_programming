#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    pepe = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return my_list
    pepe[idx] = element
    
    return pepe
