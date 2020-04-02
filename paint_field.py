from PyQt5.QtGui import QBrush, QColor, QPolygon
from PyQt5.QtCore import QPoint

from hexagon import make_hexagon


def paint_hexagons(painter, arr, x0, y0, hex_a):

    for i in arr.items():
        if i[1] == 'white':
            painter.setBrush(QBrush(QColor(255, 255, 255)))
        elif i[1] == 'red':
            painter.setBrush(QBrush(QColor(255, 0, 0)))
        else:
            painter.setBrush(QBrush(QColor(0, 0, 255)))

        painter.drawPolygon(make_hexagon(x0 + i[0][0] * hex_a,
                                         y0 + i[0][1] * hex_a, hex_a))


def paint_triangle(points, painter):
    triangle = QPolygon()
    for i in points:
        triangle.append(i)
    painter.drawPolygon(triangle)


def paint_triangles(painter, field_rang, x0, y0, hex_a):

    point_a = QPoint(x0 + hex_a, y0 - 2 * hex_a)
    point_b = QPoint(x0 + (field_rang + 2) * hex_a,
                     y0 + ((field_rang - 1) * 2 + 1.5) * hex_a)
    point_c = QPoint(x0 + hex_a,
                     y0 + ((field_rang + 1) + field_rang * 3) * hex_a)
    point_d = QPoint(x0 - field_rang * hex_a,
                     y0 + ((field_rang - 1) * 2 + 1.5) * hex_a)
    point_o = QPoint(x0 + hex_a, y0 + ((field_rang - 1) * 2 + 1.5) * hex_a)

    painter.setBrush(QColor(255, 0, 0))

    paint_triangle([point_a, point_b, point_o], painter)
    paint_triangle([point_c, point_d, point_o], painter)

    painter.setBrush(QColor(0, 0, 255))

    paint_triangle([point_b, point_c, point_o], painter)
    paint_triangle([point_d, point_a, point_o], painter)


def paint_field(painter, arr, field_rang, x0, y0, hex_a):

    paint_triangles(painter, field_rang, x0, y0, hex_a)

    paint_hexagons(painter, arr, x0, y0, hex_a)
