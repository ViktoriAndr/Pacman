import unittest

from Direction import Direction
from Game import Game
from Map import Map
from Pacman import Pacman


class TestPacman(unittest.TestCase):
    def setUp(self):
        super(TestPacman, self).setUp()
        self.game = Game()
        self.map = Map()

    def test_pacman_move_right(self):
        self.game.pacman.move(Direction.Right)
        self.assertEqual(self.game.pacman.coord.x, 14)
        self.assertEqual(self.game.pacman.coord.y, 23)

    def test_pacman_move_left(self):
        self.game.pacman.move(Direction.Left)
        self.assertEqual(self.game.pacman.coord.x, 12)
        self.assertEqual(self.game.pacman.coord.y, 23)

    def test_pacman_move_up(self):
        self.game.pacman.move(Direction.Up)
        self.assertEqual(self.game.pacman.coord.x, 13)
        self.assertEqual(self.game.pacman.coord.y, 23)

    def test_pacman_move_down(self):
        self.game.pacman.move(Direction.Down)
        self.assertEqual(self.game.pacman.coord.x, 13)
        self.assertEqual(self.game.pacman.coord.y, 23)

    def test_portal_1(self):
        self.game_1 = Game()
        self.game_1.pacman = Pacman(self.map.portal_point[0][0]+1, self.map.portal_point[0][1])
        self.game_1.move_pacman()
        self.game_1.pacman.move(Direction.Left)
        self.assertEqual(self.game_1.pacman.coord.x, self.map.width-1)

    def test_portal_2(self):
        self.game_2 = Game()
        self.game_2.pacman = Pacman(self.map.portal_point[1][0]-1, self.map.portal_point[1][1])
        self.game_2.move_pacman()
        self.assertEqual(self.game_2.pacman.coord.x, 0)

    def test_ball_point(self):
        self.game_3 = Game()
        self.game_3.move_pacman()
        self.game_3.move_pacman()
        self.game_3.move_pacman()
        self.game_3.move_pacman()
        self.assertTrue(self.game_3.map.map[int(self.game_3.pacman.coord.x - 1)][self.game_3.pacman.coord.y], None)

    def test_energizer_point(self):
        self.game_4 = Game()
        self.pacman = Pacman(self.game_4.energizer_point[0].coord.x, self.game_4.energizer_point[0].coord.y)
        self.game_4.pacman.move(Direction.Down)
        self.game_4.pacman.move(Direction.Down)
        self.game_4.pacman.move(Direction.Down)
        self.game_4.pacman.move(Direction.Down)
        self.assertTrue(self.game_4.map.map[int(self.game_4.pacman.coord.x)][self.game_4.pacman.coord.y - 1], None)

if __name__ == '__main__':
    unittest.main()
