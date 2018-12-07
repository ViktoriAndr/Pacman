import sys

from Food import Ball, Energizer
from Ghost import Ghost
from Graph import *
from Map import Map
from Pacman import *


class Game:
    def __init__(self):
        self.game_over = False
        self.map = Map()
        self.graph = Graph()
        self.ball_point = []
        self.energizer_point = []

        for i in range(self.map.height):
            for j in range(self.map.width):
                if self.map.map[i][j] == '@':
                    self.pacman = Pacman(j, i)
                elif self.map.map[i][j] == '1':
                    self.Blinky = Ghost(j, i)
                elif self.map.map[i][j] == '2':
                    self.Inky = Ghost(j, i)
                elif self.map.map[i][j] == '3':
                    self.Pinky = Ghost(j, i)
                elif self.map.map[i][j] == '4':
                    self.Clyde = Ghost(j, i)
                elif self.map.map[i][j] == '.':
                    self.ball = Ball(j, i)
                    self.ball_point.append(self.ball)
                elif self.map.map[i][j] == '*':
                    self.energizer = Energizer(j, i)
                    self.energizer_point.append(self.energizer)

    def move_ghost_chase(self):
        self.Blinky.search_path(self.graph, (self.Blinky.coord.x, self.Blinky.coord.y),
                                (self.pacman.coord.x, self.pacman.coord.y))
        self.Pinky.search_path(self.graph, (self.Pinky.coord.x, self.Pinky.coord.y),
                               (self.pacman.coord.x, self.pacman.coord.y))
        self.Inky.search_path(self.graph, (self.Inky.coord.x, self.Inky.coord.y),
                              (self.pacman.coord.x, self.pacman.coord.y))
        self.Clyde.search_path(self.graph, (self.Clyde.coord.x, self.Clyde.coord.y),
                               (self.pacman.coord.x, self.pacman.coord.y))

    def move_ghost_scatter(self):
        if self.Blinky.coord.x != 24 and self.Blinky.coord.y != 1:
            self.Blinky.search_path(self.graph, (self.Blinky.coord.x, self.Blinky.coord.y), (24, 1))
        else:
            self.Blinky.move((25, 1))
            self.Blinky.search_path(self.graph, (self.Blinky.coord.x, self.Blinky.coord.y), (24, 1))

        if self.Pinky.coord.x != 3 and self.Pinky.coord.y != 1:
            self.Pinky.search_path(self.graph, (self.Pinky.coord.x, self.Pinky.coord.y), (3, 1))
        else:
            self.Pinky.move((4, 1))
            self.Pinky.search_path(self.graph, (self.Pinky.coord.x, self.Pinky.coord.y), (3, 1))

        if self.Inky.coord.x != 20 and self.Inky.coord.y != 23:
            self.Inky.search_path(self.graph, (self.Inky.coord.x, self.Inky.coord.y), (20, 23))
        else:
            self.Inky.move((21, 23))
            self.Inky.search_path(self.graph, (self.Inky.coord.x, self.Inky.coord.y), (20, 23))

        if self.Clyde.coord.x != 7 and self.Clyde.coord.y != 23:
            self.Clyde.search_path(self.graph, (self.Clyde.coord.x, self.Clyde.coord.y), (7, 23))
        else:
            self.Clyde.move((8, 23))
            self.Clyde.search_path(self.graph, (self.Clyde.coord.x, self.Clyde.coord.y), (7, 23))

    def move_pacman(self):
        self.pacman.move(self.pacman.route)
        for ball in self.ball_point:
            if ball.coord.x == self.pacman.coord.x and ball.coord.y == self.pacman.coord.y:
                self.pacman.mark += ball.count
                self.ball_point.remove(ball)

        for invisibility in self.energizer_point:
            if invisibility.coord.x == self.pacman.coord.x and invisibility.coord.y == self.pacman.coord.y:
                self.pacman.mark += invisibility.count
                self.energizer_point.remove(invisibility)

        if (self.pacman.coord.x == self.Blinky.coord.x and self.pacman.coord.y == self.Blinky.coord.y) \
                or (self.pacman.coord.x == self.Inky.coord.x and self.pacman.coord.y == self.Inky.coord.y) \
                or (self.pacman.coord.x == self.Pinky.coord.x and self.pacman.coord.y == self.Pinky.coord.y) \
                or (self.pacman.coord.x == self.Clyde.coord.x and self.pacman.coord.y == self.Clyde.coord.y):
            self.pacman.live -= 1


if __name__ == '__main__':
    Game()
    sys.exit()
