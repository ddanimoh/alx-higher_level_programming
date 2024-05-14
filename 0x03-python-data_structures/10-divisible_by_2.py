#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    ls = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            ls.append(True)
        else:
            ls.append(False)
    return ls
