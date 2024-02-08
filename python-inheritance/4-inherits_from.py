#!/usr/bin/python3

'''
Module that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
'''


def inherits_from(obj, a_class):
    '''
    that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
    '''
    if isinstance(obj, a_class):
        return True
    elif issubclass(obj, a_class):
        return False
    else:
        return False