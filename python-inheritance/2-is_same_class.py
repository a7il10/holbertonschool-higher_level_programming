#!/usr/bin/python3

'''
Module that returns True if the object is exactly an instance
'''


def is_same_class(obj, a_class):
    '''
    that returns True if the object is exactly an instance
    '''
    return type(obj) is a_class
