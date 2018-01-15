from PyQt4.QtGui import *
from PyQt4 import QtGui
from Color import Color
from Tile import Tile

class Background():
    def __init__(self, window):
        self.window = window
        self.data = None
        self.x = None
        self.y = None
        self.length = None
        self.tilesPerRow = 4
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
        self.x = self.getWidth() * 0.05
        self.length = self.getWidth() - (self.x * 2)
        self.y = self.getHeight() - self.length - self.x
        rectRounding = self.length / 100
        painter.setBrush(Color.gridBackground)
        painter.drawRoundedRect(self.x, self.y, self.length, self.length, rectRounding, rectRounding)

    def drawEmptyTiles(self, painter):
        print "Grid background (startX, startY, endX, endY): ({}, {}, {}, {})".format(self.x, self.y, self.x + self.length, self.y + self.length)
        painter.setBrush(Color.emptyTile)
        offset = self.length / 60
        rectRounding = self.length / 150
        tileLength = (self.length / self.tilesPerRow) - (offset * (1.0 + (1.0 / self.tilesPerRow)))
        rectCount = 0
        self.grid = []
        for tileX in xrange(0, self.tilesPerRow):
            for tileY in xrange(0, self.tilesPerRow):
                startX = offset + self.x + (tileLength * tileX) + (offset * tileX)
                startY = offset + self.y + (tileLength * tileY) + (offset * tileY)
                self.grid.append(tileX, tileY, startX, startY)
                painter.drawRoundedRect(startX, startY, tileLength, tileLength, rectRounding, rectRounding)
                rectCount += 1
                endX = startX + tileLength
                endY = startY + tileLength
                print "Tile background {0:2} (startX, startY, endX, endY): ({1:7.3f}, {2:7.3f}, {3:7.3f}, {4:7.3f})".format(rectCount, startX, startY, endX, endY)

    def getWidth(self):
        return self.window.width()

    def getHeight(self):
        return self.window.height()