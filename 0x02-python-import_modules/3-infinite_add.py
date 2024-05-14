#!/usr/bin/python3
import sys

if __name__ == '__main__':

    sum = 0
    arr = sys.argv
    for x in range(1, len(arr)):
        sum += int(arr[x])
    print("{:}".format(sum))
