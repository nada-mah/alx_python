"""this module houses the square class that inherts from rectangle class"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """A square class that inherits from rectangle class"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
    
    def __dir__ (cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        """Returns the area of the square"""
        return self.__size**2
    