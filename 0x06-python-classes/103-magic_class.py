#!/usr/bin/python3

'''
comment stay here for model
'''
import math


class MagicClass:
    '''
    classs comment dho;ud be here
    '''

    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius  # sets the _MagicClass__radius attribute

    def area(self):
        return (self.__radius ** 2) * math.pi  # calculates area of the circle

    def circumference(self):
        return 2 * math.pi * self.__radius
