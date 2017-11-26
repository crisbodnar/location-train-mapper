from typing import List
import math


class Coordinate(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
    
    @property
    def y(self, ):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def similar(self, other_coord) -> bool:
        delta = 0.0001
        return math.fabs(self.x - other_coord.x) <= delta and math.fabs(self.y - other_coord.y) <= delta

    def distance(self, other_ccord) -> float:
        return math.sqrt((other_ccord.x - self.x)**2 + (other_ccord.y - self.y)**2)

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)


def coord_in_array(coords: List[Coordinate], coord: Coordinate) -> bool:
    for other_coord in coords:
        if other_coord.similar(coord):
            return True
    return False

