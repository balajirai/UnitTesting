# Using parametrizing in testing

import math
from .my_fixtures import Rectangle


class Square(Rectangle):


    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        
