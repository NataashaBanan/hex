from unittest.mock import Mock

try:
    from PyQt5.QtCore import QPoint
    from PyQt5.QtGui import QPolygon
except SystemExit:
    QPoint = Mock()
    QPolygon = Mock()


def create_hexagon(x0, y0, hex_a):
    polygon = QPolygon()
    polygon.append(QPoint(x0, y0 + hex_a))
    polygon.append(QPoint(x0 + hex_a, y0))
    polygon.append(QPoint(x0 + 2 * hex_a, y0 + hex_a))
    polygon.append(QPoint(x0 + 2 * hex_a, y0 + 2 * hex_a))
    polygon.append(QPoint(x0 + hex_a, y0 + 3 * hex_a))
    polygon.append(QPoint(x0, y0 + 2 * hex_a))
    return polygon
