from update_field import update_dict
# import pytest


class Test_little_dict():
    def test_not_in_field(self):
        my_dict, turn = update_dict(-1, -1, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

        my_dict, turn = update_dict(0, 0, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

        my_dict, turn = update_dict(10, 0, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

        my_dict, turn = update_dict(20, 0, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

        my_dict, turn = update_dict(0, 10, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

        my_dict, turn = update_dict(0, 15, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

        my_dict, turn = update_dict(10, 30, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'white'})
        assert (turn == 'red')

    def test_in_field(self):
        my_dict, turn = update_dict(10, 5, {(0, 0): 'white'}, 'red', 0, 0, 10)
        assert (my_dict == {(0, 0): 'red'})
        assert (turn == 'blue')

        my_dict, turn = update_dict(10, 5, {(0, 0): 'white'}, 'blue', 0, 0, 10)
        assert (my_dict == {(0, 0): 'blue'})
        assert (turn == 'red')

    def test_colored_field(self):
        my_dict, turn = update_dict(10, 5, {(0, 0): 'red'}, 'blue', 0, 0, 10)
        assert (my_dict == {(0, 0): 'red'})
        assert (turn == 'blue')

        my_dict, turn = update_dict(10, 5, {(0, 0): 'blue'}, 'blue', 0, 0, 10)
        assert (my_dict == {(0, 0): 'blue'})
        assert (turn == 'blue')

    def test_empty_field(self):
        my_dict, turn = update_dict(10, 5, {}, 'blue', 0, 0, 10)
        assert (my_dict == {})
        assert (turn == 'blue')
