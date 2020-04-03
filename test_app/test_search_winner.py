from app.search_winner import is_winner
from app.game import Game
from app.turn_and_color import Color


class TestLittleField():

    def test_1_rang_field(self):
        game = Game()
        game.rang = 1
        game.hex_dictionary = {(0, 0): Color.Red}
        assert (is_winner(game))
        game.hex_dictionary = {(0, 0): Color.White}
        assert (not is_winner(game))
        game.hex_dictionary = {(0, 0): Color.Blue}
        assert (not is_winner(game))
        game.turn.another_turn()
        assert(is_winner(game))

    def test_2_rang_field(self):
        game = Game()
        game.rang = 2
        game.hex_dictionary = {(0, 0): Color.White,
                               (-1, 2): Color.Red,
                               (1, 2): Color.Red, (0, 4): Color.Blue}
        assert (is_winner(game))


class TestRealGame():
    def test(self):
        game = Game()
        game.hex_dictionary = {(0, 0): Color.Red,
                               (-1, 2): Color.Red,
                               (1, 2): Color.Red,
                               (-2, 4): Color.Blue,
                               (0, 4): Color.Red,
                               (2, 4): Color.Blue,
                               (-3, 6): Color.Red,
                               (-1, 6): Color.Red,
                               (1, 6): Color.Red,
                               (3, 6): Color.Red,
                               (-4, 8): Color.Blue,
                               (-2, 8): Color.Red,
                               (0, 8): Color.Blue, (2, 8): Color.Blue,
                               (4, 8): Color.Red,
                               (-5, 10): Color.Red,
                               (-3, 10): Color.Blue,
                               (-1, 10): Color.White,
                               (1, 10): Color.Blue,
                               (3, 10): Color.Blue, (5, 10): Color.Blue,
                               (-6, 12): Color.Red,
                               (-4, 12): Color.Red,
                               (-2, 12): Color.Blue,
                               (0, 12): Color.Blue,
                               (2, 12): Color.Red, (4, 12): Color.Red,
                               (6, 12): Color.Blue,
                               (-7, 14): Color.Red,
                               (-5, 14): Color.Blue,
                               (-3, 14): Color.Blue,
                               (-1, 14): Color.Blue,
                               (1, 14): Color.Blue, (3, 14): Color.Blue,
                               (5, 14): Color.Red,
                               (7, 14): Color.White,
                               (-8, 16): Color.Blue,
                               (-6, 16): Color.Red,
                               (-4, 16): Color.Blue,
                               (-2, 16): Color.Red, (0, 16): Color.Blue,
                               (2, 16): Color.Blue, (4, 16): Color.Blue,
                               (6, 16): Color.Blue,
                               (8, 16): Color.Red,
                               (-9, 18): Color.Red,
                               (-7, 18): Color.Red,
                               (-5, 18): Color.Blue,
                               (-3, 18): Color.Red,
                               (-1, 18): Color.Blue, (1, 18): Color.Blue,
                               (3, 18): Color.White, (5, 18): Color.Blue,
                               (7, 18): Color.Red,
                               (9, 18): Color.Red,
                               (-10, 20): Color.Red,
                               (-8, 20): Color.Blue,
                               (-6, 20): Color.Red,
                               (-4, 20): Color.Blue,
                               (-2, 20): Color.Blue, (0, 20): Color.Red,
                               (2, 20): Color.Blue, (4, 20): Color.Blue,
                               (6, 20): Color.Blue,
                               (8, 20): Color.Red,
                               (10, 20): Color.Red, (0, 40): Color.Red,
                               (-1, 38): Color.Red, (1, 38): Color.Red,
                               (-2, 36): Color.Red, (0, 36): Color.Red,
                               (2, 36): Color.Red,
                               (-3, 34): Color.Red,
                               (-1, 34): Color.Red, (1, 34): Color.Blue,
                               (3, 34): Color.Red,
                               (-4, 32): Color.Red,
                               (-2, 32): Color.Blue, (0, 32): Color.Red,
                               (2, 32): Color.Red, (4, 32): Color.Red,
                               (-5, 30): Color.Red,
                               (-3, 30): Color.Blue,
                               (-1, 30): Color.Blue,
                               (1, 30): Color.Blue, (3, 30): Color.Blue,
                               (5, 30): Color.Blue,
                               (-6, 28): Color.Red,
                               (-4, 28): Color.Red,
                               (-2, 28): Color.Blue,
                               (0, 28): Color.Blue, (2, 28): Color.Blue,
                               (4, 28): Color.Red, (6, 28): Color.Red,
                               (-7, 26): Color.Red,
                               (-5, 26): Color.Blue,
                               (-3, 26): Color.Red,
                               (-1, 26): Color.Red, (1, 26): Color.Blue,
                               (3, 26): Color.Blue, (5, 26): Color.Red,
                               (7, 26): Color.Red,
                               (-8, 24): Color.Red,
                               (-6, 24): Color.Blue,
                               (-4, 24): Color.Blue,
                               (-2, 24): Color.Blue, (0, 24): Color.Blue,
                               (2, 24): Color.Blue, (4, 24): Color.White,
                               (6, 24): Color.Blue,
                               (8, 24): Color.Blue,
                               (-9, 22): Color.Blue,
                               (-7, 22): Color.Red,
                               (-5, 22): Color.Red,
                               (-3, 22): Color.Blue,
                               (-1, 22): Color.Red,
                               (1, 22): Color.Blue, (3, 22): Color.Blue,
                               (5, 22): Color.Blue,
                               (7, 22): Color.White, (9, 22): Color.Red}
        game.turn.another_turn()
        assert (is_winner(game))
