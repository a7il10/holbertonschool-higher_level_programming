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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        self.__size == value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
                print("#" * self.size)
