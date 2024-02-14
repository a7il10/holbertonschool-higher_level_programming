#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """class Square that inherits from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update Square"""
        attributes = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            if i < len(attributes):
                setattr(self, attributes[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """to dictionary"""
        return {
            'id': self.id,
            'size': self.__width,
            'x': self.__x,
            'y': self.__y
        }
