#!/usr/bin/python3

'''
Write a class Square that defines a square
'''


class Square:
    '''
    Private instance attribute: size
    '''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size * self.__size
