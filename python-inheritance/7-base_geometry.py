#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """Defines an empty class"""
    def area(self):
        """Improve geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method: def integer_validator(self, name, value):
            that validates value"""
        if type(value) is not int:
            TypeError(f"{name} must be an integer")
        if value <= 0:
            ValueError(f"{name} must be greater than 0")
