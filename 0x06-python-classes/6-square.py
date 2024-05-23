#!/usr/bin/python3

"""
A defination of Square class

"""


class Square:
    """
    A class with a private attribute size
    With instantiation of 0, with Error check condition
    """

    def __init__(self, size=0, position=(0, 0)):

        if not (isinstance(position[0], int) and isinstance(position[1], int)):
            raise TypeError("position must be a
                            tuple of 2 positive integers")
        if len(position) < 2 or posision[0] < 0 or position[1] < 0:
            raise TypeError("position must be a
                            tuple of 2 positive integers")
        self.__position = position
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
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

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__potision = value
