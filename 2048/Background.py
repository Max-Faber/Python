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
        self.setBackgroundsBackground()
        painter.end()

    def setBackgroundsBackground(self):
        self.data.fill(QtGui.QColor(202, 192, 180))