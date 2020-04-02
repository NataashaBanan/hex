from is_winner import is_winner


class Test_little_field():
    def test_1_rang_field(self):
        assert (is_winner({(0, 0): 'red'}, 'red', 1))

        assert (not is_winner({(0, 0): 'white'}, 'blue', 1))

    def test_2_rang_field(self):
        assert (is_winner({(0, 0): 'white', (-1, 2): 'red',
                           (1, 2): 'red', (0, 4): 'blue'}, 'red', 2))


class Test_real_game():
    def test(self):
        assert (is_winner(
            {(0, 0): 'red', (-1, 2): 'red', (1, 2): 'red', (-2, 4): 'blue',
             (0, 4): 'red', (2, 4): 'blue', (-3, 6): 'red', (-1, 6): 'red',
             (1, 6): 'red', (3, 6): 'red', (-4, 8): 'blue', (-2, 8): 'red',
             (0, 8): 'blue', (2, 8): 'blue', (4, 8): 'red', (-5, 10): 'red',
             (-3, 10): 'blue', (-1, 10): 'white', (1, 10): 'blue',
             (3, 10): 'blue', (5, 10): 'blue', (-6, 12): 'red',
             (-4, 12): 'red', (-2, 12): 'blue', (0, 12): 'blue',
             (2, 12): 'red', (4, 12): 'red', (6, 12): 'blue', (-7, 14): 'red',
             (-5, 14): 'blue', (-3, 14): 'blue', (-1, 14): 'blue',
             (1, 14): 'blue', (3, 14): 'blue', (5, 14): 'red',
             (7, 14): 'white', (-8, 16): 'blue', (-6, 16): 'red',
             (-4, 16): 'blue', (-2, 16): 'red', (0, 16): 'blue',
             (2, 16): 'blue', (4, 16): 'blue', (6, 16): 'blue', (8, 16): 'red',
             (-9, 18): 'red', (-7, 18): 'red', (-5, 18): 'blue',
             (-3, 18): 'red', (-1, 18): 'blue', (1, 18): 'blue',
             (3, 18): 'white', (5, 18): 'blue', (7, 18): 'red', (9, 18): 'red',
             (-10, 20): 'red', (-8, 20): 'blue', (-6, 20): 'red',
             (-4, 20): 'blue', (-2, 20): 'blue', (0, 20): 'red',
             (2, 20): 'blue', (4, 20): 'blue', (6, 20): 'blue', (8, 20): 'red',
             (10, 20): 'red', (0, 40): 'red', (-1, 38): 'red', (1, 38): 'red',
             (-2, 36): 'red', (0, 36): 'red', (2, 36): 'red', (-3, 34): 'red',
             (-1, 34): 'red', (1, 34): 'blue', (3, 34): 'red', (-4, 32): 'red',
             (-2, 32): 'blue', (0, 32): 'red', (2, 32): 'red', (4, 32): 'red',
             (-5, 30): 'red', (-3, 30): 'blue', (-1, 30): 'blue',
             (1, 30): 'blue', (3, 30): 'blue', (5, 30): 'blue',
             (-6, 28): 'red', (-4, 28): 'red', (-2, 28): 'blue',
             (0, 28): 'blue', (2, 28): 'blue', (4, 28): 'red', (6, 28): 'red',
             (-7, 26): 'red', (-5, 26): 'blue', (-3, 26): 'red',
             (-1, 26): 'red', (1, 26): 'blue', (3, 26): 'blue', (5, 26): 'red',
             (7, 26): 'red', (-8, 24): 'red', (-6, 24): 'blue',
             (-4, 24): 'blue', (-2, 24): 'blue', (0, 24): 'blue',
             (2, 24): 'blue', (4, 24): 'white', (6, 24): 'blue',
             (8, 24): 'blue', (-9, 22): 'blue', (-7, 22): 'red',
             (-5, 22): 'red', (-3, 22): 'blue', (-1, 22): 'red',
             (1, 22): 'blue', (3, 22): 'blue', (5, 22): 'blue',
             (7, 22): 'white', (9, 22): 'red'}, 'blue', 11))
