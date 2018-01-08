import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from Game import Game
from Background import Background

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    widget = QWidget()
    widget.resize(500, 600)

    game = Game(widget)
    background = Background(widget)
    game.setBackground(background)
    layout = QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.addWidget(game)
    widget.setLayout(layout)
    widget.setWindowTitle("2048")
    widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    widget.show()
    sys.exit(app.exec_())
