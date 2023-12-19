""""
Rectangle classs
"""
from models.base import Base
class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
    @property
    def width(self):
        '''public method: Returns the size of the square'''
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        '''public method: Returns the size of the square'''
        return self.__height
    
    @height.setter
    def size(self, height):
        self.__height = height
    
    @property
    def x(self):
        '''public method: Returns the size of the square'''
        return self.__x
    
    @size.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        '''public method: Returns the size of the square'''
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
