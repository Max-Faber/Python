from PyQt4 import QtGui, uic

uiFile = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)

class Game(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.background = None

    def draw(self, qp):
        qp.setBrush(QtGui.QColor(178, 168, 158))
        qp.drawRect(100, 100, 100, 100)
        qp.end()
        qp.begin(self)
        qp.drawPixmap(0, 0, self.background)
        qp.end()
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self.background)
        pen = QtGui.QPen()
        pen.setStyle(0)
        qp.setPen(pen)
        self.draw(qp)

    def setBackground(self, bg):
        self.background = bg