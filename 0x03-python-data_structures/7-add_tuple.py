#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)

    a = len(tuple_a)
    b = len(tuple_b)

    if a == 1:
        tuple_a.append(0)
    elif a == 0:
        tuple_a.append(0)
        tuple_a.append(0)

    if b == 1:
        tuple_b.append(0)
    elif b == 0:
        tuple_b.append(0)
        tuple_b.append(0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
