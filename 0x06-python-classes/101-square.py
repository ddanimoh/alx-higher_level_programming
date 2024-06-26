#!/usr/bin/python3
'''
Continue class sqr
'''


class Square:

    '''
    Comment for class comes here explain what the class does
    '''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print(self.__str__())

    def __str__(self):
        if self.__size == 0:
            return ""

        result = []
        # Append the leading new lines based on position[1]
        result.append("\n" * self.__position[1])

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size + "\n")

        return "".join(result).rstrip()
