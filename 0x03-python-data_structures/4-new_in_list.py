#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    li = my_list[:]

    ln = -1 + len(li)

    if idx > ln or idx < 0:
        return li

    li[idx] = element
    return li
