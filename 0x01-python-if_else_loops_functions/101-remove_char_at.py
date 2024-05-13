#!/usr/bin/python3

def remove_char_at(str, n):

    ls = list(str)

    if n > -1 + len(str) or n < 0:
        return str

    for x in ls:

        if x == str[n]:
            del ls[n]
            continue
    return "".join(ls)
