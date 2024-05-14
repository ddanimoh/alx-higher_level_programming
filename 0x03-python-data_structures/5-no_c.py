#!/usr/bin/python3

def no_c(my_string):

    lis = [x for x in my_string if x not in "cC"]
    lis = "".join(lis)
    return lis
