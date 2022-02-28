import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow

from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

        self.coords = []

    def run(self):
        x, y, r = randint(0, 750), randint(0, 550), randint(1, 400)
        color_r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.coords.append(((x, y, r, r), (color_r, g, b)))
        self.repaint()

    def draw_circle(self, qp):

        for i in self.coords:
            qp.setBrush(QColor(*i[1]))
            qp.drawEllipse(*i[0])

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
