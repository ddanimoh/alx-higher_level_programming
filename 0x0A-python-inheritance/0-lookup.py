#!/usr/bin/python3
"""
This module provides a function to list the
available attributes and methods of an object.

Functions:
    lookup(obj): Returns a list of available attributes and
    methods of the given object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the names of the attributes
        and methods of the object.
    """
    return dir(obj)
