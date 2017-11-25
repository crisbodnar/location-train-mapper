from typing import List


class Coordinate(object):
    delta = 0.0001
    
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
        return self.x - other_coord.x <= self.delta and self.y - other_coord.y <= self.delta

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)


def coord_in_array(coords: List[Coordinate], coord: Coordinate) -> bool:
    for other_coord in coords:
        if other_coord.similar(coord):
            return True
    return False

