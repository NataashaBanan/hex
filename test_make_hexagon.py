from PyQt5.QtGui import QPolygon

from hexagon import make_hexagon


class Test_making_hexagon():
    def test_make_hex(self):
        hexagon = make_hexagon(0, 0, 5)
        assert (isinstance(hexagon, QPolygon))
        assert (hexagon.count() == 6)
