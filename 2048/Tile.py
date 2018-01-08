from random import randint

class Tile():
    def __init__(self):
        self.value = self.generateNewValue()

    def generateNewValue(self):
        if randint(1, 2) == 1:
            return 2
        else:
            return 4