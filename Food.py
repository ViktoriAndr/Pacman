from Point import Point


class Ball:
    def __init__(self, x, y):
        self.coord = Point(x, y)
        self.count = 10


class Energizer:
    def __init__(self, x, y):
        self.coord = Point(x, y)
        self.count = 50
