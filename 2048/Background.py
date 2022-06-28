from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtGui
from Color import Color
from Tile import Tile


class Background:
    def __init__(self, window):
        self.window = window
        self.data = None
        self.x = None
        self.y = None
        self.length = None
        self.tilesPerRow = 8
        self.grid = [[None for _ in range(self.tilesPerRow)] for _ in range(self.tilesPerRow)]

    def generateBackground(self, width, height):
        self.data = QPixmap(width, height)
        painter = QPainter()
        painter.begin(self.data)
        pen = QtGui.QPen()
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
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
        offset: float = self.length / 60
        rectRounding: float = self.length / 150
        tileLength: float = (self.length / self.tilesPerRow) - (offset * (1.0 + (1.0 / self.tilesPerRow)))

        for tileX in range(self.tilesPerRow):
            for tileY in range(self.tilesPerRow):
                startX = offset + self.x + (tileLength * tileX) + (offset * tileX)
                startY = offset + self.y + (tileLength * tileY) + (offset * tileY)
                painter.drawRoundedRect(startX, startY, tileLength, tileLength, rectRounding, rectRounding)
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
