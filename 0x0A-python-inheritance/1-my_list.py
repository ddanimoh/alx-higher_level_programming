#!/usr/bin/python3

"""
This module provides a class MyList that inherits from the built-in
list class.

Classes:
    MyList: A subclass of list with an additional method to print
    the list in sorted order.
"""

class MyList(list):
    """
    A subclass of list with an additional method to print
    the list in sorted order.
    
    Methods:
        print_sorted(): Prints the list sorted in ascending order.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Assumes all elements in the list are of type int.
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
