"""This module houses a function that checks if an  object is exactly an instance of the specified class """

def is_same_class(obj, a_class):
    '''Check if an object is exactly an instance of the specified class'''
    return (type(obj) == a_class)
