#!/usr/bin/python3

for x in range(0, 9):
    for c in range(0, 10):
        if x < c and x != 8:
            print("{:}{:}, ".format(x, c), end='')
print("{:}{:}".format(x, c))
