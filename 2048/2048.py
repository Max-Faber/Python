import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from Game import Game
from Background import Background

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    widget: QWidget = QWidget()
    widget.resize(500, 700)

    game: Game = Game(widget)
    game.setBackground(Background(widget))
    layout: QVBoxLayout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(game)
    widget.setLayout(layout)
    widget.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
    widget.setWindowTitle("2048")
    widget.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
    widget.show()
    sys.exit(app.exec())
