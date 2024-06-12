#!/usr/bin/python3

'''
A square class with private instance with Method
'''


class Square:

    '''
    A class with a private attribute size
    With instantiation of 0, with Error check condition
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print()
            return

        [print() for _ in range(self._position[1])]
        for i in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
