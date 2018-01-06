from PyQt4 import QtGui, uic
from PyQt4.QtGui import QSizePolicy
from Color import Color
import time

uiFile = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)

class Game(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.setMinimumWidth(250)
        #self.setMinimumHeight(300)
        self.background = None
        self.painter = None

    def draw(self):
        self.painter.setBrush(Color.emptyTile)
        self.painter.drawRoundedRect(100, 400, 50, 50, 10, 10)
        self.painter.end()
        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.background.data)
        self.painter.end()

    def paintEvent(self, event):
        self.painter = QtGui.QPainter()
        self.painter.begin(self.background.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        self.painter.setPen(pen)
        self.draw()

    def resizeEvent(self, *args, **kwargs):
        self.setMinimumHeight(self.width())
        print str(self.minimumHeight())
        self.background.generateBackground(self.width(), self.height())

    def mouseReleaseEvent(self, *args, **kwargs):
        if self.resized:
            ratio = 5.0 / 6.0
            self.background.generateBackground(self.width(), self.height())
            self.resize(self.width(), self.width() / ratio)

    def setBackground(self, bg):
        self.background = bg
