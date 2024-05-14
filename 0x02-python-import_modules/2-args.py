#!/usr/bin/python3
import sys

if __name__ == '__main__':

    le = len(sys.argv)
    if le - 1 == 0:
        print("{:} {:}".format(le - 1, 'arguments.'))
    elif le - 1 == 1:
        print("{:} {:}".format(le - 1, 'argument:'))
    else:
        print("{:} {:}".format(le - 1, 'arguments:'))

    for x in range(1, le):
        print("{:}: {:}".format(x, sys.argv[x]))
