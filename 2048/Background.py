from PyQt4.QtGui import *
from PyQt4 import QtGui
from Color import Color

class Background():
    def __init__(self, window):
        self.window = window
        self.data = None
        self.x = None
        self.y = None
        self.length = None

    def generateBackground(self, width, height):
        self.data = QPixmap(width, height)
        painter = QPainter()
        painter.begin(self.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        painter.setPen(pen)
        self.setBackgroundsBackground()
        self.drawGridBackground(painter)
        self.drawEmptyTiles(painter)
        painter.end()

    def setBackgroundsBackground(self):
        self.data.fill(Color.widgetBackground)

    def drawGridBackground(self, painter):
        self.x = self.getWidth() / 25.0
        self.y = self.getHeight() / 5.0
        self.length = self.getHeight() - self.y - self.x
        painter.setBrush(Color.gridBackground)
        painter.drawRoundedRect(self.x, self.y, self.length, self.length, 10, 10)

    def drawEmptyTiles(self, painter):
        painter.setBrush(Color.emptyTile)
        offset = self.length / 60
        tilesPerRow = 4
        tileLength = (self.length / tilesPerRow) - (offset * 2)
        drawCount = 0
        for tileX in xrange(0, tilesPerRow):
            for tileY in xrange(0, tilesPerRow):
                if tileX == 0 and tileY == 0:
                    painter.drawRoundedRect(offset + self.x, offset + self.y, tileLength, tileLength, 5, 5)
                    drawCount += 1
                    print drawCount
                elif tileX == 0 and tileX + 1 != tilesPerRow:
                    painter.drawRoundedRect(self.x + (tileLength + (offset * (tileX + 1))), self.y + (tileLength + (offset * (tileY + 1))), tileLength, tileLength, 5, 5)
                    drawCount += 1
                    print drawCount


                #else:
                #    painter.drawRoundedRect(offset + self.x + tileLength * (tileX + 1), offset + self.y + tileLength * (tileY + 1), tileLength, tileLength, 5, 5)

    def getWidth(self):
        return self.window.width()

    def getHeight(self):
        return self.window.height()
