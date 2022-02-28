import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.run)

        self.coords = []

    def run(self):
        x, y, r = randint(0, 750), randint(0, 550), randint(1, 400)
        self.coords.append((x, y, r, r))
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(Qt.yellow)

        for i in self.coords:
            qp.drawEllipse(*i)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
