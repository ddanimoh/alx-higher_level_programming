#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    ln = -1 + len(my_list)

    if idx > ln or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
