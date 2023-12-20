'''
Square class
'''
from models.rectangle import Rectangle

class Square(Rectangle):
    ''''
    This class models a Square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        '''public method: gets the size of the square '''
        return self.width
    @size.setter
    def size(self, size):
        if not type(size)==int:
            raise TypeError('width must be an integer')
        elif size <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = size