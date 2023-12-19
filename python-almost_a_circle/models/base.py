"""
base class
"""

class Base:
    '''
    This class will be the “base” of all other classes in this project.
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        """
        manage id attribute in all your future classes
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects