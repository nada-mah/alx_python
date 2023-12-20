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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        '''public method: Returns the width of the Rectangle '''
        return self.__width
    
    @width.setter
    def width(self, width):
        if not type(width)==int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
    
    @property
    def height(self):
        '''public method: Returns the height of the Rectangle'''
        return self.__height
    
    @height.setter
    def height(self, height):
        if not type(height)==int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
    
    @property
    def x(self):
        '''public method: Returns the x of the Rectangle'''
        return self.__x
    
    @x.setter
    def x(self, x):
        if not type(x)==int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
    
    @property
    def y(self):
        '''public method: Returns the y of the Rectangle'''
        return self.__y
    
    @y.setter
    def y(self, y):
        if not type(y)==int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
            
    def area(self):
        '''public method: Returns the area of the Rectangle''' 
        return self.width * self.height
    
    def display(self):
        ''' public method: that prints in stdout the Rectangle instance with the character #'''
        for i in range(self.height):
            print('#'*self.width)
            
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)