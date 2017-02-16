#!/usr/bin/env python3


class Block(object):
    def __init__(self, width, height, **attr):
        self.__width = width
        self.__height = height

    def __eq__(self, another):
        return (self.__width == another.__width) and \
               (self.__height == another.__height)


class Brick(Block):
    pass


class Layer(Block):
    def build(self, brick, **more):

        pass


class Wall(Block):
    pass




class WallBuilder(object):
    def __init__(self, brick, *more):
        self.__bricks = [brick]
        for i in more:
            if i not in self.__bricks:
                self.__bricks.append(i)


def get(x, y, z):
    m1 = (z//x)
    m2 = (z//y)
    return [(i, j) for i in range(0, m1+1) for j in range(0, m2+1) if (x*i + y*j) == z]

b1 = Brick(2, 1)
b2 = Brick(3, 1)

c = WallBuilder(b1, b2)

pass
