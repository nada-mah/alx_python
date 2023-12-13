"""This module houses a class that represents a square """
class Square:
    """Represents a Square with Size 
    size should be an integer and greater than zero"""
    __size = None
    def __init__(self,size=0):
        if isinstance(size,int):
            self.__size = size
        else:
            raise TypeError('size must be an integer')
        if size >= 0:
            self.__size = size
        else:
            raise ValueError('size must be >= 0')

