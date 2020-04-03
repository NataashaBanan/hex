from app.game import Game
from app.create_hexagon_dict import make_hex_dict
from app.turn_and_color import Turn, Color


class TestGame():
    def test_creation(self):
        game = Game()
        game.hex_dictionary = make_hex_dict(11)
        game.rang = 11
        game.turn = Turn(Color.Red)
        game.win = False

    def test_new_rang(self, n=5):
        game = Game()
        game.new_rang(n)
        assert(game.rang == n)
        assert (game.hex_dictionary == make_hex_dict(n))

    def test_update_with_win(self):
        game = Game()
        game.win = True
        a = game.hex_dictionary.copy()
        game.update_game(0, 0)
        assert (a == game.hex_dictionary)

    def test_simple_update(self):
        game = Game()
        game.hot_seat = True
        game.update_game(235, 325)
        assert (game.hex_dictionary == {
            (0, 0): Color.White,
            (-1, 2): Color.White,
            (1, 2): Color.White,
            (-2, 4): Color.White,
            (0, 4): Color.White,
            (2, 4): Color.White,
            (-3, 6): Color.White,
            (-1, 6): Color.White,
            (1, 6): Color.White,
            (3, 6): Color.White,
            (-4, 8): Color.White,
            (-2, 8): Color.White,
            (0, 8): Color.White,
            (2, 8): Color.White,
            (4, 8): Color.White,
            (-5, 10): Color.White,
            (-3, 10): Color.White,
            (-1, 10): Color.White,
            (1, 10): Color.White,
            (3, 10): Color.White,
            (5, 10): Color.White,
            (-6, 12): Color.White,
            (-4, 12): Color.White,
            (-2, 12): Color.White,
            (0, 12): Color.White,
            (2, 12): Color.White,
            (4, 12): Color.White,
            (6, 12): Color.White,
            (-7, 14): Color.White,
            (-5, 14): Color.White,
            (-3, 14): Color.White,
            (-1, 14): Color.White,
            (1, 14): Color.White,
            (3, 14): Color.White,
            (5, 14): Color.White,
            (7, 14): Color.White,
            (-8, 16): Color.White,
            (-6, 16): Color.White,
            (-4, 16): Color.White,
            (-2, 16): Color.White,
            (0, 16): Color.White,
            (2, 16): Color.White,
            (4, 16): Color.White,
            (6, 16): Color.White,
            (8, 16): Color.White,
            (-9, 18): Color.White,
            (-7, 18): Color.White,
            (-5, 18): Color.White,
            (-3, 18): Color.White,
            (-1, 18): Color.White,
            (1, 18): Color.White,
            (3, 18): Color.White,
            (5, 18): Color.White,
            (7, 18): Color.White,
            (9, 18): Color.White,
            (-10, 20): Color.Red,
            (-8, 20): Color.White,
            (-6, 20): Color.White,
            (-4, 20): Color.White,
            (-2, 20): Color.White,
            (0, 20): Color.White,
            (2, 20): Color.White,
            (4, 20): Color.White,
            (6, 20): Color.White,
            (8, 20): Color.White,
            (10, 20): Color.White,
            (0, 40): Color.White,
            (-1, 38): Color.White,
            (1, 38): Color.White,
            (-2, 36): Color.White,
            (0, 36): Color.White,
            (2, 36): Color.White,
            (-3, 34): Color.White,
            (-1, 34): Color.White,
            (1, 34): Color.White,
            (3, 34): Color.White,
            (-4, 32): Color.White,
            (-2, 32): Color.White,
            (0, 32): Color.White,
            (2, 32): Color.White,
            (4, 32): Color.White,
            (-5, 30): Color.White,
            (-3, 30): Color.White,
            (-1, 30): Color.White,
            (1, 30): Color.White,
            (3, 30): Color.White,
            (5, 30): Color.White,
            (-6, 28): Color.White,
            (-4, 28): Color.White,
            (-2, 28): Color.White,
            (0, 28): Color.White,
            (2, 28): Color.White,
            (4, 28): Color.White,
            (6, 28): Color.White,
            (-7, 26): Color.White,
            (-5, 26): Color.White,
            (-3, 26): Color.White,
            (-1, 26): Color.White,
            (1, 26): Color.White,
            (3, 26): Color.White,
            (5, 26): Color.White,
            (7, 26): Color.White,
            (-8, 24): Color.White,
            (-6, 24): Color.White,
            (-4, 24): Color.White,
            (-2, 24): Color.White,
            (0, 24): Color.White,
            (2, 24): Color.White,
            (4, 24): Color.White,
            (6, 24): Color.White,
            (8, 24): Color.White,
            (-9, 22): Color.White,
            (-7, 22): Color.White,
            (-5, 22): Color.White,
            (-3, 22): Color.White,
            (-1, 22): Color.White,
            (1, 22): Color.White,
            (3, 22): Color.White,
            (5, 22): Color.White,
            (7, 22): Color.White,
            (9, 22): Color.White}
                )

    def test_to_win_update(self):
        game = Game()
        game.new_rang(2)
        game.hex_dictionary = {(0, 0): Color.White, (-1, 2): Color.Red,
                               (1, 2): Color.Blue, (0, 4): Color.White}
        game.update_game(399, 249)
        assert (game.hex_dictionary == {(0, 0): Color.Red,
                                        (-1, 2): Color.Red,
                                        (1, 2): Color.Blue,
                                        (0, 4): Color.White})
        assert game.win
        assert game.newRecord

    def test_to_lose_update(self):
        game = Game()
        game.new_rang(2)
        game.hex_dictionary = {(0, 0): Color.White,
                               (-1, 2): Color.Blue,
                               (1, 2): Color.White,
                               (0, 4): Color.Red}
        game.update_game(389, 243)
        assert game.win
        assert not game.newRecord

    def test_undo_history(self):
        game = Game()
        game.hot_seat = True
        game.new_rang(2)
        game.update_game(389, 243)
        game.update_game(331, 344)
        assert (game.undo_history ==
                [((0, 0), Color.Red), ((-1, 2), Color.Blue)])
        game.undo()
        assert (game.undo_history == [((0, 0), Color.Red)])
        assert (game.redo_history == [((-1, 2), Color.Blue)])
        game.undo()
        assert (game.undo_history == [])
        assert (game.redo_history ==
                [((-1, 2), Color.Blue), ((0, 0), Color.Red)])
        game.undo()
        assert (game.undo_history == [])
        assert (game.redo_history ==
                [((-1, 2), Color.Blue), ((0, 0), Color.Red)])
        game.update_game(356, 324)
        assert (game.redo_history == [])
