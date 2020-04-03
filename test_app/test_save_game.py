from app.save_game import load, save
from app.game import Game
from app.turn_and_color import Turn, Color


import shutil
import os


class TestSaveGame():

    def prepare_test(self):
        try:
            shutil.rmtree(os.path.join(os.getcwd(), 'saves'))
        except FileNotFoundError:
            pass
        os.mkdir('saves')

    def test_save_and_load(self):
        self.prepare_test()

        game = Game()
        save('a', game)
        game.new_rang(2)
        save('b', game)
        game.hot_seat = True
        save('c', game)
        game.turn.another_turn()
        save('d', game)

        new_game = Game()
        load(new_game, 3)
        assert new_game.hot_seat
        assert new_game.rang == 2
        assert new_game.turn.color == Color.Blue

        load(new_game, 2)
        assert new_game.turn.color == Color.Red

        load(new_game, 1)
        assert not new_game.hot_seat

        load(new_game, 0)
        assert new_game.rang == 11

    def test_right_hex_dictionary(self):
        self.prepare_test()

        game = Game()
        game.new_rang(2)
        diction = {(0, 0): Color.White, (-1, 2): Color.Red,
                   (1, 2): Color.Red, (0, 4): Color.Blue}
        game.hex_dictionary = diction.copy()

        save('a', game)

        new_game = Game()
        load(new_game, 0)
        assert new_game.hex_dictionary == diction
