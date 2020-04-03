from app.create_hexagon_dict import make_hex_dict
from app.turn_and_color import Color


class TestDict():
    def test_right_format(self):
        hex_dict = make_hex_dict(4)
        assert(isinstance(hex_dict, dict))
        for key in hex_dict.keys():
            assert(isinstance(key, tuple))
            assert(len(key) == 2)
            assert(isinstance(key[0], int))
            assert(isinstance(key[1], int))
            value = hex_dict[key]
            assert(isinstance(value, Color))

        arr = list(filter(lambda x: x == Color.White, hex_dict.values()))
        assert (len(hex_dict) == len(arr))

    def test_right_count(self):
        for x in range(2, 20):
            assert(len(make_hex_dict(x).items()) == x * (x - 1) + x)
