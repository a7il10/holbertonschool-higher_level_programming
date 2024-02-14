#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """class Square that inherits from Rectangle"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """str"""
        return (f"[Square] ({id}) {x}/{y} - "
                f"{size}")
