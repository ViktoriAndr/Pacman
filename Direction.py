import enum

from Point import Point


class Direction(enum.Enum):
    Right = Point(1, 0)
    Left = Point(-1, 0)
    Up = Point(0, -1)
    Down = Point(0, 1)
