from enum import Enum


class Color(Enum):
    White = 0
    Red = 1
    Blue = 2


class Turn:
    def __init__(self, color=Color.Red):
        self.color = color

    def another_turn(self):
        if self.color == Color.Red:
            self.color = Color.Blue
        else:
            self.color = Color.Red

    def __str__(self):
        if self.color == Color.Red:
            return "Red"
        return "Blue"
