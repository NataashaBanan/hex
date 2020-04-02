from make_hex_arr import make_hex_dict


class Test_dict():
    def test_right_format(self):
        hex_dict = make_hex_dict(4)
        isinstance(hex_dict, dict)
        isinstance(list(hex_dict.values())[0], str)
        arr = list(filter(lambda x: x == 'white', hex_dict.values()))
        assert (len(hex_dict) == len(arr))

    def test_right_count(self):
        for x in range(2, 20):
            assert(len(make_hex_dict(x).items()) == x * (x - 1) + x)
