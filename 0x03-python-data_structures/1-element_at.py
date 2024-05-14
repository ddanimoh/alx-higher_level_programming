#!/usr/bin/python3

def element_at(my_list, idx):

    ln = -1 + len(my_list)

    if idx > ln or idx < 0:
        return None
    return my_list[idx]
