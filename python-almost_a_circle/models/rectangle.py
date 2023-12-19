""""
Rectangle classs
"""
from models.base import Base
class Rectangle(Base):
    ''''
    This class models a rectangle
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
    @property
    def width(self):
        '''public method: Returns the width of the Rectangle '''
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width
    
    @property
    def height(self):
        '''public method: Returns the height of the Rectangle'''
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height
    
    @property
    def x(self):
        '''public method: Returns the x of the Rectangle'''
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        '''public method: Returns the y of the Rectangle'''
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
