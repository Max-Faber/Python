from PyQt4 import QtGui, uic
from Color import Color

uiFile = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)

class Game(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.backgroundSet = False
        self.background = None

    def draw(self, qp):
        if self.backgroundSet:
            qp.setBrush(Color.emptyTile)
            qp.drawRoundedRect(100, 400, 50, 50, 10, 10)
            qp.end()
            qp.begin(self)
            qp.drawPixmap(0, 0, self.background.data)
            qp.end()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self.background.data)
        pen = QtGui.QPen()
        pen.setStyle(0)
        qp.setPen(pen)
        self.draw(qp)

    def resizeEvent(self, *args, **kwargs):
        if self.checkRatio() is True:
            self.background.generateBackground()

    def setBackground(self, bg):
        self.background = bg
        self.backgroundSet = True

    def checkRatio(self):
        wantedRatio = 5.0 / 6.0
        width = self.width() * 1.0
        height = self.height() * 1.0
        actualRatio = width / height
        if wantedRatio != actualRatio:
            print "Width: " + str(width)
            print "Height: " + str(width / wantedRatio)
            print width / wantedRatio
            self.resize(width, width / wantedRatio)
            return True
