#!/usr/bin/python3
"""inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
