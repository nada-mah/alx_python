""" module houses rectangle class"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    '''rectangle object class inherits from BaseGeometry'''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def area(self):
        ''' return area of rectangle (width*height)'''
        return self.__width * self.__height