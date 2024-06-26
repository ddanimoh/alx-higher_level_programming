#!/usr/bin/python3

def roman_to_int(roman_string):

    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rome = 0
    prev_value = 0

    if isinstance(roman_string, int) or roman_string is None:
        return 0

    for char in roman_string:
        current_value = dic[char]
        if prev_value < current_value:
            rome += current_value - 2 * prev_value
        else:
            rome += current_value
        prev_value = current_value
    return rome
