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
        self.grid = [[None for y in xrange(4)] for x in xrange(4)]

    def generateBackground(self, width, height):
        self.data = QPixmap(width, height)
        painter = QPainter()
        painter.begin(self.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing)
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
        painter.setBrush(Color.emptyTile)
        offset = self.length / 60
        rectRounding = self.length / 150
        tileLength = (self.length / self.tilesPerRow) - (offset * (1.0 + (1.0 / self.tilesPerRow)))
        rectCount = 0
        for tileX in xrange(0, self.tilesPerRow):
            for tileY in xrange(0, self.tilesPerRow):
                startX = offset + self.x + (tileLength * tileX) + (offset * tileX)
                startY = offset + self.y + (tileLength * tileY) + (offset * tileY)
                painter.drawRoundedRect(startX, startY, tileLength, tileLength, rectRounding, rectRounding)
                rectCount += 1
                if self.grid[tileX][tileY] is None:
                    self.grid[tileX][tileY] = Tile(startX, startY, tileLength, rectRounding)
                else:
                    self.grid[tileX][tileY].x = startX
                    self.grid[tileX][tileY].y = startY
                    self.grid[tileX][tileY].length = tileLength
                    self.grid[tileX][tileY].rectRounding = rectRounding

    def getWidth(self):
        return self.window.width()

    def getHeight(self):
        return self.window.height()

    def getGrid(self):
        return self.grid
