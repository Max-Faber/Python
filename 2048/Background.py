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
        self.grid = None

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
        self.x = self.getWidth() / (1.1)
        self.length = self.getWidth() - (self.x * 2)
        self.y = self.getHeight() - self.length - self.x
        rectRounding = self.length / 100
        painter.setBrush(Color.gridBackground)
        painter.drawRoundedRect(self.x, self.y, self.length, self.length, rectRounding, rectRounding)

    def drawEmptyTiles(self, painter):
        print "Grid background (startX, startY, endX, endY): (" + str(self.x) + ", " + str(self.y) + ", " + str(self.x + self.length) + ", " + str(self.y + self.length) + ")"
        painter.setBrush(Color.emptyTile)
        offset = self.length / 60
        print "Offset: " + str(offset)
        rectRounding = self.length / 150
        tilesPerRow = 4
        tileLength = (self.length / tilesPerRow) - (offset * (1.0 + (1.0 / tilesPerRow)))
        rectCount = 0
        for tileX in xrange(0, tilesPerRow):
            for tileY in xrange(0, tilesPerRow):
                painter.drawRoundedRect(offset + self.x + (tileLength * tileX) + (offset * tileX), offset + self.y + (tileLength * tileY) + (offset * tileY), tileLength, tileLength, rectRounding, rectRounding)
                rectCount += 1
                startX = offset + self.x + (tileLength * tileX) + (offset * tileX)
                startY = offset + self.y + (tileLength * tileY) + (offset * tileY)
                endX = startX + tileLength
                endY = startY + tileLength
                print "Rect " + str(rectCount) + " (startX, startY, endX, endY): (" + str(startX) + ", " + str(startY) + ", " + str(endX) + ", " + str(endY) + ")"

    def getWidth(self):
        return self.window.width()

    def getHeight(self):
        return self.window.height()

