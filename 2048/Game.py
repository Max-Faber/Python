from Color import Color
from PyQt4.QtGui import *
from random import randint
from PyQt4 import QtGui, QtCore
import copy

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
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

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
            self.newTile(2)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            gridBefore = copy.deepcopy(self.grid)
            self.moveGridUp()
            if not self.gridsAreEqual(gridBefore, self.grid):
                self.newTile(1)
                self.repaint()
        elif event.key() == QtCore.Qt.Key_Down:
            gridBefore = copy.deepcopy(self.grid)
            self.moveGridDown()
            if not self.gridsAreEqual(gridBefore, self.grid):
                self.newTile(1)
                self.repaint()
        elif event.key() == QtCore.Qt.Key_Left:
            gridBefore = copy.deepcopy(self.grid)
            self.moveGridLeft()
            if not self.gridsAreEqual(gridBefore, self.grid):
                self.newTile(1)
                self.repaint()
        elif event.key() == QtCore.Qt.Key_Right:
            gridBefore = copy.deepcopy(self.grid)
            self.moveGridRight()
            if not self.gridsAreEqual(gridBefore, self.grid):
                self.newTile(1)
                self.repaint()
        elif event.key() == QtCore.Qt.Key_Space:
            row = [16, 8, 8, 4]
            self.combineRow(row)
            row = [4, 4, 8, 4]
            self.combineRow(row)

    def gridsAreEqual(self, grid, grid2):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileX in range(xMax):
            for tileY in range(yMax):
                if grid[tileX][tileY].value is not grid2[tileX][tileY].value:
                    return False
        return True

    def moveGridUp(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileX in range(xMax):
            row = []
            for tileY in range(yMax):
                row.append(self.grid[tileX][tileY].value)
            row = self.combineRow(row)
            for i in range(len(row)):
                self.grid[tileX][i].value = row[i]

    def moveGridDown(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileX in range(xMax):
            row = []
            for tileY in range(yMax - 1, -1, -1):
                row.append(self.grid[tileX][tileY].value)
            row = self.combineRow(row)
            for i in range(len(row)):
                self.grid[tileX][len(row) - 1 - i].value = row[i]

    def moveGridLeft(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileY in range(yMax):
            row = []
            for tileX in range(xMax):
                row.append(self.grid[tileX][tileY].value)
            row = self.combineRow(row)
            for i in range(len(row)):
                self.grid[i][tileY].value = row[i]

    def moveGridRight(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileY in range(yMax):
            row = []
            for tileX in range(xMax - 1, -1, -1):
                row.append(self.grid[tileX][tileY].value)
            row = self.combineRow(row)
            for i in range(len(row)):
                self.grid[len(row) - 1 - i][tileY].value = row[i]

    def combineRow(self, row):
        print "Start row: " + str(row)
        for i in range(len(row)):
            if row[i] is not None:
               for j in range(i):
                    if row[j] is None:
                        row[j] = row[i]
                        row[i] = None
                    elif row[j] is not None:
                        if row[j] == row[i] and self.selectionIsEmpty(row, j, i):
                            row[j] = row[j] + row[i]
                            for k in range(i, len(row) - 1):
                                row[k] = row[k + 1]
                            row[len(row) - 1] = None
        print "End row: " + str(row) + "\n"
        return row

    def selectionIsEmpty(self, row, begin, end):
        if begin > end:
            begin, end = self.swap(begin, end)
        for i in range(begin + 1, end):
            if row[i] is not None:
                return False
        return True

    def swap(self, numb, numb2):
        temp = numb
        numb = numb2
        numb2 = temp
        return numb, numb2

    def heightForWidth(self, width):
        ratio = 5.0 / 7.0
        self.window.setMaximumHeight(width / ratio)
        return width / ratio

    def setBackground(self, bg):
        self.background = bg

    def updateGrid(self):
        xMax = len(self.grid)
        yMax = len(self.grid[len(self.grid) - 1])

        for tileX in range(xMax):
            for tileY in range(yMax):
                if self.grid[tileX][tileY].value is not None:
                    self.painter.setBrush(Color().getTileColor(self.grid[tileX][tileY].value))
                    self.painter.drawRoundedRect(self.grid[tileX][tileY].x,
                                                 self.grid[tileX][tileY].y,
                                                 self.grid[tileX][tileY].length,
                                                 self.grid[tileX][tileY].length,
                                                 self.grid[tileX][tileY].rectRounding,
                                                 self.grid[tileX][tileY].rectRounding)
                    self.painter.setPen(QtGui.QColor(0, 0, 0))
                    self.painter.setFont(QtGui.QFont('clear-sans', 30))
                    self.painter.drawText(self.grid[tileX][tileY].x,
                                          self.grid[tileX][tileY].y,
                                          self.grid[tileX][tileY].length,
                                          self.grid[tileX][tileY].length,
                                          QtCore.Qt.AlignCenter,
                                          str(self.grid[tileX][tileY].value))
                    self.painter.setPen(0)

    def newTile(self, tileCount):
        for count in range(tileCount):
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

