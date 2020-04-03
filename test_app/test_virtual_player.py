from app.virtual_player import random_computer_turn, smart_computer_turn
from app.game import Game
from app.turn_and_color import Color


class TestOnLittleField():
    def test_1_rang_field(self):
        game = Game()
        game.rang = 1
        game.hex_dictionary = {(0, 0): Color.White}
        random_computer_turn(game)
        assert (game.hex_dictionary == {(0, 0): Color.Red})
        game.hex_dictionary = {(0, 0): Color.White}
        smart_computer_turn(game)
        assert (game.hex_dictionary == {(0, 0): Color.Red})

    def test_2_rang_field(self):
        game = Game()
        game.rang = 2
        start = {(0, 0): Color.White, (-1, 2): Color.Red,
                 (1, 2): Color.Red, (0, 4): Color.Blue}
        result = {(0, 0): Color.Red, (-1, 2): Color.Red, (1, 2): Color.Red,
                  (0, 4): Color.Blue}
        game.hex_dictionary = start.copy()
        random_computer_turn(game)
        assert (game.hex_dictionary == result)
        game.hex_dictionary = start
        smart_computer_turn(game)
        assert (game.hex_dictionary == result)
