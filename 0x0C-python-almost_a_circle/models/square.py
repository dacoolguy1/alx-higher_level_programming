#!/usr/bin/python3
"""
square module
inherits its  properties from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializes instances"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """special method"""
        str_rect = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} ".format(self.x, self.y)
        str_size = "- {}/{}".format(self.width, self.height)
        return str_rect + str_id + str_xy + str_size
