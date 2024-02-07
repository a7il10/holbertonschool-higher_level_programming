#!/usr/bin/python3
def inherits_from(obj, a_class):
    if isinstance(obj, a_class):
        return True
    elif issubclass(obj, a_class):
        return False
    else:
        return False