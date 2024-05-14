#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    hidden = dir(hidden_4)

    for x in range(len(hidden)):
        if hidden[x][0] != '_' and hidden[x][1] != '_':
            print(hidden[x])
