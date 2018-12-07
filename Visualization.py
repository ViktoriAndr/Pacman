import pickle
import sys

from PyQt5.QtCore import QRectF, Qt, QBasicTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush, QIcon, QPen, QPalette, QImage, QFont

from Direction import Direction
from Game import Game

TITLE = "Pacman"
ICON = "Icon.png"
WIDTH = 672
HEIGHT = 744+50
CELL_SIZE = 24


class DrawMap(QWidget):
    def __init__(self):
        super().__init__()
        self.game = Game()
        self.timer = 0
        self.timer_mode = 0
        self.timer_ghost_start = 0
        self.timer_Blinky = 0
        self.timer_Pinky = 0
        self.timer_Inky = 0
        self.timer_Clyde = 0
        self.timer = QBasicTimer()
        self.timer.start(150, self)

        self.setFixedSize(WIDTH, HEIGHT)
        self.center()
        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon(ICON))
        pal = self.palette()
        pal.setColor(QPalette.Normal, QPalette.Background, QColor("black"))
        self.setPalette(pal)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.status_bar(painter)
        self.creating_map(painter)
        self.draw_elements(painter)
        painter.end()

    def status_bar(self, painter):
        for i in range(self.game.pacman.live):
            pacman_live = QImage("images/Right.png")
            painter.drawImage(i * CELL_SIZE, 31.5 * CELL_SIZE, pacman_live)

        painter.setPen(QColor(168, 34, 3))
        painter.setFont(QFont('Decorative', 15))
        painter.drawText(CELL_SIZE, CELL_SIZE, 300, 1490, Qt.AlignCenter, "Points: " + str(self.game.pacman.mark))

        save = QPushButton("Save", self)
        save.resize(90, 30)
        save.move(23.5*CELL_SIZE, 31.5 * CELL_SIZE)
        save.clicked.connect(self._save)
        save.show()

        load = QPushButton("Load", self)
        load.resize(90, 30)
        load.move(19 * CELL_SIZE, 31.5 * CELL_SIZE)
        load.show()
        load.clicked.connect(self._load)

    def _save(self):
        output = open('data', 'wb')
        pickle.dump(self.game, output, 2)
        output.close()

    def _load(self):
        input = open('data', 'rb')
        self.game = pickle.load(input)
        input.close()

    def creating_map(self, painter):
        for i in range(self.game.map.height):
            for j in range(self.game.map.width):
                self.draw_map(painter, self.game.map.map, i, j)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

    def draw_map(self, painter, map, i, j):
        col = QColor(255, 255, 255)
        col.setNamedColor('#d4d4d4')
        painter.setPen(col)

        if map[i][j] == '#':
            painter.setBrush(QBrush(QColor("dark blue")))
            painter.drawRect(QRectF(CELL_SIZE * j, CELL_SIZE * i, CELL_SIZE, CELL_SIZE))

        elif map[i][j] == '&':
            painter.setBrush(QBrush(QColor("pink")))
            painter.drawRect(QRectF(CELL_SIZE * j, (CELL_SIZE * i) + CELL_SIZE / 2,
                                    CELL_SIZE, CELL_SIZE / 2))

    def draw_elements(self, painter):
        for ball in self.game.ball_point:
            painter.setBrush(QBrush(QColor("yellow")))
            painter.drawEllipse(QRectF((CELL_SIZE * ball.coord.x) + CELL_SIZE // 3,
                                       (CELL_SIZE * ball.coord.y) + CELL_SIZE // 3,
                                       CELL_SIZE // 3, CELL_SIZE // 3))

        for energizer in self.game.energizer_point:
            painter.setBrush(QBrush(QColor("white")))
            painter.drawEllipse(QRectF((CELL_SIZE * energizer.coord.x) + CELL_SIZE // 5,
                                       (CELL_SIZE * energizer.coord.y) + CELL_SIZE // 5,
                                       CELL_SIZE // 1.5, CELL_SIZE // 1.5))

        image_pacman = QImage("images/Right.png")
        painter.drawImage(self.game.pacman.coord.x * CELL_SIZE,
                          self.game.pacman.coord.y * CELL_SIZE, image_pacman)

        image_ghost_red = QImage("images/Blinky.png")
        painter.drawImage(self.game.Blinky.coord.x * CELL_SIZE,
                          self.game.Blinky.coord.y * CELL_SIZE, image_ghost_red)

        image_ghost_blue = QImage("images/Inky.png")
        painter.drawImage(self.game.Inky.coord.x * CELL_SIZE,
                          self.game.Inky.coord.y * CELL_SIZE, image_ghost_blue)

        image_ghost_pink = QImage("images/Pinky.png")
        painter.drawImage(self.game.Pinky.coord.x * CELL_SIZE,
                          self.game.Pinky.coord.y * CELL_SIZE, image_ghost_pink)

        image_ghost_orange = QImage("images/Clyde.png")
        painter.drawImage(self.game.Clyde.coord.x * CELL_SIZE,
                          self.game.Clyde.coord.y * CELL_SIZE, image_ghost_orange)

    def keyPressEvent(self, event):
        if event.nativeVirtualKey() == Qt.Key_D:
            self.game.pacman.move(Direction.Right)
        elif event.nativeVirtualKey() == Qt.Key_W:
            self.game.pacman.move(Direction.Up)
        elif event.nativeVirtualKey() == Qt.Key_S:
            self.game.pacman.move(Direction.Down)
        elif event.nativeVirtualKey() == Qt.Key_A:
            self.game.pacman.move(Direction.Left)

    def keyReleaseEvent(self, event):
        if event.nativeVirtualKey() == Qt.Key_D:
            self.game.pacman.move(Direction.Right)
        elif event.nativeVirtualKey() == Qt.Key_W:
            self.game.pacman.move(Direction.Up)
        elif event.nativeVirtualKey() == Qt.Key_S:
            self.game.pacman.move(Direction.Down)
        elif event.nativeVirtualKey() == Qt.Key_A:
            self.game.pacman.move(Direction.Left)

    def timerEvent(self, *args, **kwargs):
        self.game.move_pacman()

        if self.timer_mode <= 270:
            self.ghost_mode()
        else:
            self.timer_mode = 0
            self.ghost_mode()

        self.Blinky_move()
        self.Pinky_move()

        if self.timer_ghost_start < 80:
            self.timer_ghost_start += 1
        else:
            self.Inky_move()
            self.Clyde_move()

        self.update()

    @staticmethod
    def zeroize_timer(timer):
        if timer > 1000:
            return 0
        return timer

    def ghost_mode(self):
        if self.timer_mode <= 70:
            self.game.move_ghost_scatter()
            self.timer_mode += 1
        if 71 <= self.timer_mode <= 270:
            self.game.move_ghost_chase()
            self.timer_mode += 1

    def Blinky_move(self):
        self.timer_Blinky = self.zeroize_timer(self.timer_Blinky)
        save_B = 1
        for i in range(len(self.game.Blinky.path)):
            i = save_B
            if self.timer_Blinky % 2 == 0:
                self.game.Blinky.move(self.game.Blinky.path[i])
            else:
                save_B = i
        self.timer_Blinky += 1

    def Pinky_move(self):
        self.timer_Pinky = self.zeroize_timer(self.timer_Pinky)
        save_P = 1
        for i in range(len(self.game.Pinky.path)):
            i = save_P
            if self.timer_Pinky % 2 == 0:
                self.game.Pinky.move(self.game.Pinky.path[i])
            else:
                save_P = i
        self.timer_Pinky += 1

    def Inky_move(self):
        self.timer_Inky = self.zeroize_timer(self.timer_Inky)
        save_I = 1
        for i in range(len(self.game.Inky.path)):
            i = save_I
            if self.timer_Inky % 2 == 0:
                self.game.Inky.move(self.game.Inky.path[i])
            else:
                save_I = i
        self.timer_Inky += 1

    def Clyde_move(self):
        self.timer_Clyde = self.zeroize_timer(self.timer_Clyde)
        save_C = 1
        for i in range(len(self.game.Clyde.path)):
            i = save_C
            if self.timer_Clyde % 2 == 0:
                self.game.Clyde.move(self.game.Clyde.path[i])
            else:
                save_C = i
        self.timer_Clyde += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawMap()
    sys.exit(app.exec_())
