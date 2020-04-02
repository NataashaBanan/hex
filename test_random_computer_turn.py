from computer_player import random_computer_turn


class Test_on_little_field():
    def test_1_rang_field(self):
        assert (random_computer_turn({(0, 0): 'white'}, 'red')
                == {(0, 0): 'red'})

        assert (random_computer_turn({(0, 0): 'white'}, 'blue')
                == {(0, 0): 'blue'})
