#!/usr/bin/python3
'''
Module to define a rectangle
'''


class Rectangle:
    '''
    define a rectangle
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        print_str = ""
        if self.width == 0 or self.height == 0:
            return print_str
        else:
            for h in range(self.height - 1):
                print_str += self.print_symbol * self.width + "\n"
            print_str += self.print_symbol * self.width
            return print_str

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    