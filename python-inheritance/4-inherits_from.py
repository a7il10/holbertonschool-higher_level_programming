#!/usr/bin/python3

'''
Module that returns True if the object is an instance
'''


def inherits_from(obj, a_class):
    '''
    that returns True if the object is an instance
    '''
    if isinstance(obj, a_class):
        return True
    elif issubclass(obj, a_class):
        return False
    else:
        return False
