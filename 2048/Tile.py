from random import randint

class Tile():
    def __init__(self, x, y, length, rectRounding):
        self.value = None
        self.x = x
        self.y = y
        self.rectRounding = rectRounding
        self.length = length

    def generateNewValue(self):
        if randint(1, 2) == 1:
            return 2
        else:
            return 4