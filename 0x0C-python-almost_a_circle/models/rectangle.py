#!/usr/bin/python3
"""Module that contain class rectangle that inherits
from class base
"""
from models.base import Base


class Rectangle(Base):
    """
    it inherits its properties from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is the height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Thus us the height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is the x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """This is the x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is the y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """This is the y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle using special character"""
        for juse in range(self.__y):
            print()
        for i in range(self.__height):
            for y in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """override main string method"""
        str_rect = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rect + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """update function, we will use setattr function"""
        if args is not None and len(args) is not 0:
            list_atr = ["id", "width", "height", "x", "y"]
            for items in range(len(args)):
                setattr(self, list_atr[items], args[items])
        else:
            for keys, values in kwargs.items():
                setattr(self, keys, value)
