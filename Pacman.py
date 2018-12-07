from Direction import Direction
from Map import Map
from Point import *
from Wall import Wall


class Pacman:
    def __init__(self, x, y):
        self.coord = Point(x, y)
        self.live = 3
        self.end = False
        self.wall = Wall()
        self.mark = 0
        self.map = Map()
        self.route = Direction.Right

    def move(self, route):
        self.route = route
        x = route.value.x
        y = route.value.y
        while (True):
            if [self.coord.x + x, self.coord.y + y] not in self.wall.wall_point and \
                            [self.coord.x + x, self.coord.y + y] not in self.map.home_point and \
                                    0 <= self.coord.x + x <= self.map.width and \
                                    0 <= self.coord.y + y <= self.map.height:
                self.coord = self.coord + Point(x, y)
                for point in self.map.portal_point:
                    if point[0] == 0 and self.coord.x + x <= point[0] and \
                                            self.coord.y + y == point[1]:
                        self.coord = Point(self.map.width - 1, point[1])
                    elif point[0] == self.map.width - 1 and self.coord.x + x > point[0] and \
                                            self.coord.y + y == point[1]:
                        self.coord = Point(0, point[1])
            break
