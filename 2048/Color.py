from PyQt4 import QtGui

class Color():
    widgetBackground = QtGui.QColor(220, 220, 220)
    gridBackground   = QtGui.QColor(178, 168, 158)
    emptyTile        = QtGui.QColor(204, 192, 180)

    def getTileColor(self, number):
        if number == 2:
            return QtGui.QColor(238, 228, 218)
        elif number == 4:
            return QtGui.QColor(237, 224, 200)
        elif number == 8:
            return QtGui.QColor(242, 177, 121)
        elif number == 16:
            return QtGui.QColor(245, 149, 99)
        elif number == 32:
            return QtGui.QColor(246, 124, 95)
        elif number == 64:
            return QtGui.QColor(246, 94, 59)
        elif number == 128 or number == 256 or number == 512:
            return QtGui.QColor(237, 207, 114)
        else:
            return QtGui.QColor(255, 255, 255)
