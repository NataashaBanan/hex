from PyQt5.QtGui import QBrush, QColor, QPolygon
from PyQt5.QtCore import QPoint

from app.creating_hexagon import create_hexagon
from app.turn_and_color import Color


def paint_hexagons(painter, game):

    for i in game.hex_dictionary.items():
        if i[1] == Color.White:
            painter.setBrush(QBrush(QColor(255, 255, 255)))
        elif i[1] == Color.Red:
            painter.setBrush(QBrush(QColor(255, 0, 0)))
        else:
            painter.setBrush(QBrush(QColor(0, 0, 255)))

        painter.drawPolygon(create_hexagon(game.x0 + i[0][0] * game.hex_a,
                                           game.y0 + i[0][1] * game.hex_a,
                                           game.hex_a))


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


def paint_field(painter, game):

    paint_triangles(painter, game.rang, game.x0, game.y0, game.hex_a)

    paint_hexagons(painter, game)
