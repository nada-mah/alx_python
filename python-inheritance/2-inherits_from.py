"""This module houses a function that returns True if the object is an instance of a class that inherited (directly or indirectly) 
   from the specified class ; otherwise False."""
def inherits_from(obj, a_class):
    '''This checks if the object is an instance of a class that inherits from the specified class'''
    return issubclass(type(obj), a_class) and not (type(obj)==a_class)