#!/usr/bin/python3

"""
A defination of Square class

"""


class Square:
    """
    A class with a private attribute size
    With instantiation of 0, with Error check condition
    """

    def __init__(self, size=0):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
    Defination of Method Area, A public method
    """

    def area(self):
        return self.__size ** 2

    """
    Defination for getter Size
    """
    @property
    def size(self):
        return self.__size
    """
    Defination for getter Size
    """
    @size.setter
    def size(self, value=0):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
