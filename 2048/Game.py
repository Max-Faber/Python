from PyQt4 import QtGui
from Color import Color
from PyQt4.QtGui import *
from random import randint

class Game(QWidget):
    def __init__(self, window):
        QWidget.__init__(self)
        self.window = window
        self.background = None
        self.grid = None
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
        self.painter.setPen(0)
        self.updateGrid()
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
        if self.grid is None:
            self.grid = self.background.getGrid()
            self.newTile()
            self.newTile()

    def heightForWidth(self, width):
        ratio = 5.0 / 7.0
        self.window.setMaximumHeight(width / ratio)
        return width / ratio

    def setBackground(self, bg):
        self.background = bg

    def updateGrid(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileX in xrange(0, xMax):
            for tileY in xrange(0, yMax):
                if self.grid[tileX][tileY].value is not None:
                    self.setColor(self.grid[tileX][tileY].value)
                    self.painter.drawRoundedRect(self.grid[tileX][tileY].x,
                                                 self.grid[tileX][tileY].y,
                                                 self.grid[tileX][tileY].length,
                                                 self.grid[tileX][tileY].length,
                                                 self.grid[tileX][tileY].rectRounding,
                                                 self.grid[tileX][tileY].rectRounding)

    def newTile(self):
        x, y = self.getNewTilePosition()
        if x is not None or y is not None:
            self.grid[x][y].value = self.grid[x][y].generateNewValue()

    def getNewTilePosition(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])
        emptyTileCount = self.getEmptyTileCount()
        if emptyTileCount <= 0:
            return None, None
        count = 0
        random = randint(0, emptyTileCount - 1)

        for tileX in range(xMax):
            for tileY in range(yMax):
                if count == random and self.grid[tileX][tileY].value is None:
                    return tileX, tileY
                if self.grid[tileX][tileY].value is None:
                    count += 1

    def getEmptyTileCount(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])
        emptyTileCount = 0

        for tileX in xrange(0, xMax):
            for tileY in xrange(0, yMax):
                if self.grid[tileX][tileY].value is None:
                    emptyTileCount += 1
        return emptyTileCount

    def setColor(self, value):
        if value is 2:
            self.painter.setBrush(Color.two)
        elif value is 4:
            self.painter.setBrush(Color.four)
