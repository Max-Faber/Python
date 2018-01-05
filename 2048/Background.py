from PyQt4.QtGui import *
from PyQt4 import QtGui

class Background():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = QPixmap(self.width, self.height)
        self.generateBackground()

    def generateBackground(self):
        painter = QPainter()
        painter.begin(self.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        painter.setPen(pen)
        self.setBackgroundsBackground()
        self.drawGridBackground(painter)
        painter.end()

    def setBackgroundsBackground(self):
        self.data.fill(QtGui.QColor(220, 220, 220))
        #self.data.fill(QtGui.QColor(202, 192, 180))

    def drawGridBackground(self, painter):
        widthPart = self.width / 10
        heightPart = self.height / 15
        painter.setBrush(QtGui.QColor(202, 192, 180))
        painter.drawRoundedRect(widthPart, heightPart * 2, self.width - (widthPart * 2), self.height - (heightPart * 3), 30, 30)