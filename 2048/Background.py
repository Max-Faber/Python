from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from Color import Color

class Background():
    def __init__(self, window):
        self.window = window
        self.data = None
        self.generateBackground()

    def generateBackground(self, width, height):
        self.data = QPixmap(width, height)
        painter = QPainter()
        painter.begin(self.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        painter.setPen(pen)
        self.setBackgroundsBackground()
        self.drawGridBackground(painter)
        painter.end()

    def setBackgroundsBackground(self):
        self.data.fill(Color.widgetBackground)

    def drawGridBackground(self, painter):
        x = self.getWidth() / 25.0
        y = self.getHeight() / 5.0
        width = self.getWidth() - (x * 2)
        height = self.getHeight() - y - x
        painter.setBrush(Color.gridBackground)
        painter.drawRoundedRect(x, y, width, height, 10, 10)

    def getWidth(self):
        return self.window.geometry().width()

    def getHeight(self):
        return self.window.geometry().height()