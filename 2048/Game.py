from PyQt4 import QtGui
from Color import Color
from PyQt4.QtGui import *

class Game(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)
        self.window = window
        self.background = None
        self.painter = None
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        self.setMinimumWidth(250)

    def draw(self):
        self.painter.setBrush(Color.emptyTile)
        self.painter.end()
        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.background.data)
        #self.painter.drawRect(50, 50, 50, 50)
        self.painter.end()

    def paintEvent(self, event):
        self.painter = QtGui.QPainter()
        self.painter.begin(self.background.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        self.painter.setPen(pen)
        self.draw()

    def resizeEvent(self, *args, **kwargs):
        self.background.generateBackground(self.window.width(), self.window.height())

    def heightForWidth(self, width):
        ratio = 5.0 / 7.0
        self.window.setMaximumHeight(width / ratio)
        return width / ratio

    def setBackground(self, bg):
        self.background = bg
