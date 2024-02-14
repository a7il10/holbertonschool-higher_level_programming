#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)
        
    def __str__(self):
        return (f"[Square] ({id}) {x}/{y} - "
                f"{size}")
