from app.creating_hexagon import create_hexagon

from unittest.mock import Mock

try:
    from PyQt5.QtGui import QPolygon
except SystemExit as e:
    QPolygon = Mock()


class TestHex():
    def test_format(self):
        hexagon = create_hexagon(0, 0, 3)
        assert (isinstance(hexagon, QPolygon))
        assert(hexagon.count() == 6)
