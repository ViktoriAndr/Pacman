from Map import Map
from Wall import Wall
import random


class Graph:
    def __init__(self):
        self.map = Map()
        self.wall = Wall()
        self.points = []
        self.weights = {}

    def bounds(self, point):
        (x, y) = point
        return 0 <= x < self.map.width and 0 <= y < self.map.height and [x, y] not in self.wall.wall_point

    def passable(self, point):
        return point not in self.points

    def neighbors(self, point):
        (x, y) = point
        self.results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        self.results = filter(self.bounds, self.results)
        self.results = filter(self.passable, self.results)
        # self.results = self.route_x(point)
        return self.results

    def distance(self, to_node):
        return self.weights.get(to_node, 1)

    def route_x(self, point):
        (x, y) = point
        print(point)
        
        new_points = []
        for next in self.results:
            new_points.append(next)

        x_add = 0
        x_sub = 0

        for i in range(len(new_points)):
            if new_points[i] == (x + 1, y):
                x_add = (x + 1, y)
            elif new_points[i] == (x - 1, y):
                x_sub = (x - 1, y)

        if x_add != 0 and x_sub != 0:
            flag = random.choice([-1, 1])
            print("1")
            if flag == 1:
                new_points.remove((x + 1, y))
            else:
                new_points.remove((x - 1, y))

        y_add = 0
        y_sub = 0

        for i in range(len(new_points)):
            if new_points[i] == (x, y + 1):
                y_add = (x, y + 1)
            elif new_points[i] == (x, y - 1):
                y_sub = (x, y - 1)

        if y_add != 0 and y_sub != 0:
            flag = random.choice([-1, 1])
            print("2")
            if flag == 1:
                new_points.remove((x, y + 1))
            else:
                new_points.remove((x, y - 1))

        print(new_points)
        return (i for i in new_points)

