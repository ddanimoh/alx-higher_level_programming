#!/usr/bin/python3

def best_score(a_dictionary):
   
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    value = 0
    key = ''

    for x in a_dictionary:
        if a_dictionary[x] > value:
            value = a_dictionary[x]
            key = x
    return key
