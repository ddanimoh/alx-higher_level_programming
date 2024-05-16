#!/usr/bin/python3

def search_replace(my_list, search, replace):

    lst = my_list.copy()
    for x in range(len(my_list)):

        if my_list[x] == search:
            lst[x] = replace
    return lst
