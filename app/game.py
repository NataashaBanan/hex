from app.turn_and_color import Turn, Color
from app.create_hexagon_dict import make_hex_dict
from app.search_winner import is_winner
from app.virtual_player import random_computer_turn, smart_computer_turn
from app.difficulty import Difficulty


class Game:
    def __init__(self):
        self.rang = 11

        self.width = 700
        self.height = 700

        self.x0 = 350

        self.turn = Turn(Color.Red)
        self.win = False
        self.newRecord = False
        self.hot_seat = False
        self.difficult = Difficulty.easy

        self.hex_a = self.height // (4 * self.rang + 7)
        self.y0 = 4 * self.hex_a
        self.hex_dictionary = make_hex_dict(self.rang)

        self.undo_history = []
        self.redo_history = []

    def first_computer_turn(self):
        if self.difficult == Difficulty.hard:
            smart_computer_turn(self)
        else:
            random_computer_turn(self)

        self.turn.another_turn()

    def undo(self):
        if len(self.undo_history) == 0:
            return
        if not self.hot_seat and len(self.undo_history) == 1:
            return

        self.hex_dictionary[self.undo_history[-1][0]] = Color.White
        self.redo_history.append(self.undo_history[-1])
        self.undo_history.pop()
        self.turn.another_turn()

        if not self.hot_seat > 0:
            self.hex_dictionary[self.undo_history[-1][0]] = Color.White
            self.redo_history.append(self.undo_history[-1])
            self.undo_history.pop()
            self.turn.another_turn()

    def redo(self):
        if len(self.redo_history) == 0:
            return

        self.hex_dictionary[self.redo_history[-1][0]] = \
            self.redo_history[-1][1]
        self.undo_history.append(self.redo_history[-1])
        self.redo_history.pop()
        self.turn.another_turn()

        if not self.hot_seat and len(self.redo_history) > 0:
            self.hex_dictionary[self.redo_history[-1][0]] = \
                self.redo_history[-1][1]
            self.undo_history.append(self.redo_history[-1])
            self.redo_history.pop()
            self.turn.another_turn()

    def update_game(self, x, y):
        if self.win:
            return

        update = self.update_dict(x, y)

        if not update:
            return

        if is_winner(self):
            self.win = True
            self.newRecord = True
            return

        self.turn.another_turn()

        if self.hot_seat:
            return

        if self.difficult == Difficulty.hard:
            smart_computer_turn(self)
        else:
            random_computer_turn(self)

        if is_winner(self):
            self.win = True
            return
        self.turn.another_turn()

    def update_dict(self, x, y):
        for i in self.hex_dictionary.keys():
            if self.hex_dictionary[i] != Color.White:
                continue
            this_x0 = self.x0 + i[0] * self.hex_a
            this_y0 = self.y0 + i[1] * self.hex_a
            # координаты верхнего левого угла данного шестиугольника
            if x <= this_x0 or y <= this_y0 or x >= this_x0 + self.hex_a * 2 \
                    or y >= this_y0 + 3 * self.hex_a:
                continue
            # попадание в прямоугольник описанный вокруг шестиугольника
            if y <= this_y0 + self.hex_a + this_x0 - x:
                continue
            if y >= this_y0 + this_x0 + 4 * self.hex_a - x:
                continue
            if y >= this_y0 + 2 * self.hex_a + x - this_x0:
                continue
            if y <= this_y0 - self.hex_a + x - this_x0:
                continue

            self.hex_dictionary[i] = self.turn.color
            self.undo_history.append((i, self.turn.color))
            self.redo_history = []
            return True
        return False

    def new_rang(self, new_rang):
        self.rang = new_rang

        self.new_game()

    def new_game(self):
        self.turn = Turn()
        self.win = False
        self.undo_history = []
        self.redo_history = []

        self.hex_a = self.height // (4 * self.rang + 7)
        self.y0 = 4 * self.hex_a
        self.hex_dictionary = make_hex_dict(self.rang)
