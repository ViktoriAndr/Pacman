from Map import Map
from Point import *
from Queue import Queue
from Wall import Wall


class Ghost:
    def __init__(self, x, y):
        self.coord = Point(x, y)
        self.end = False
        self.wall = Wall()
        self.map = Map()

    def search_path(self, graph, start, goal):
        frontier = Queue()
        frontier.put(start, 0)
        came_from_node = {start: None}
        distance = {start: 0}

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in graph.neighbors(current):
                new_distance = distance[current] + graph.distance(next)
                if next not in distance or new_distance < distance[next]:
                    distance[next] = new_distance
                    priority = new_distance
                    frontier.put(next, priority)
                    came_from_node[next] = current

        self.reconstruct_path(came_from_node, start, goal)

    def reconstruct_path(self, came_from_node, start, goal):
        current = goal
        self.path = []
        while current != start:
            self.path.append(current)
            current = came_from_node[current]
        self.path.append(start)
        self.path.reverse()

    def move(self, point):
        x = point[0]
        y = point[1]
        self.coord = Point(x, y)


