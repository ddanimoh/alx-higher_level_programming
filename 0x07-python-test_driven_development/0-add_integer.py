#!/usr/bin/python3
"""
add_integer function adds two integers or floats
and returns the result as an integer.

The add_integer function takes two arguments,
with the second one being optional.

The result or output is always going to be an integer
even if float numbers are added.
"""


def add_integer(a, b=98):

    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number to add. Must be an int or float.
        b (int, float): The second number to add. Default is 98. Must be an int
        or float.
    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
