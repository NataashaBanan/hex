from PyQt5.QtWidgets import QWidget, QPushButton, QLCDNumber,\
    QSlider, QCheckBox
from PyQt5.QtGui import QPainter, QFont, QBrush, QColor
from PyQt5.QtCore import QPoint, Qt

from make_hex_arr import make_hex_dict
from update_field import update_field

from paint_field import paint_field
from computer_player import random_computer_turn
from is_winner import is_winner


def init_button(self, name, x0, y0, width, height, font):
    button = QPushButton(name, self)
    button.setFont(font)
    button.move(x0, y0)
    button.resize(width, height)
    button.autoFillBackground()
    button.clicked.connect(self.button_clicked)

    return button


class FieldWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.rang = 11
        self.width = 700
        self.height = 700
        self.x0 = 200
        self.turn = 'red'
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle('Hexxx')

        self.win = False
        self.hot_seat = False

        self.hex_a = self.height // (4 * self.rang + 7)
        self.y0 = 4 * self.hex_a
        self.hex_dictionary = make_hex_dict(self.rang)

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        lcd.setFixedSize(200, 100)
        lcd.smallDecimalPoint()
        lcd.move(400, 350)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setFixedSize(300, 50)
        sld.move(350, 500)
        sld.setMinimum(2)
        sld.setMaximum(20)
        sld.valueChanged[int].connect(self.change_value)

        sld.valueChanged.connect(lcd.display)

        font = QFont()
        font.setPointSize(30)
        play_button = init_button(self, 'New Game', 400, 200, 200, 100, font)

        cb = QCheckBox('Hot seat', self)
        cb.setFont(font)
        cb.move(20, 20)
        cb.setStyleSheet("QCheckBox::indicator { width:18px; height: 36px; }")
        # cb.toggle()
        cb.stateChanged.connect(self.change_mod)

    def change_mod(self, state):
        if state == Qt.Checked:
            self.hot_seat = True
        else:
            self.hot_seat = False

    def change_value(self, value):
        self.rang = value
        self.hex_a = self.height // (4 * self.rang + 7)
        self.y0 = 4 * self.hex_a
        self.hex_dictionary = make_hex_dict(self.rang)
        self.update()

    def button_clicked(self):
        # sender = self.sender()
        self.win = False
        self.hex_dictionary = make_hex_dict(self.rang)
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        font = QFont()
        font.setPointSize(32)
        painter.setFont(font)

        if self.win:
            if self.turn == "red":
                winner = "blue"
                painter.setPen(QColor(0, 0, 255))
            else:
                winner = "red"
                painter.setPen(QColor(255, 0, 0))

            font.setPointSize(40)
            painter.setFont(font)
            painter.drawText(100, 300, winner + " win")
        else:
            paint_field(painter, self.hex_dictionary,
                        self.rang, self.x0, self.y0, self.hex_a)
            if self.turn == "red":
                painter.setPen(QColor(255, 0, 0))
            else:
                painter.setPen(QColor(0, 0, 255))
            painter.drawText(420, 150, self.turn + " turn")

        painter.end()

    def mousePressEvent(self, event):
        x = (QPoint(event.pos())).x()
        y = (QPoint(event.pos())).y()

        if self.win:
            return

        self.hex_dictionary, turn, self.win = \
            update_field(x, y, self.hex_dictionary, self.turn,
                         self.rang, self.x0, self.y0, self.hex_a)
        if self.win:
            self.turn = turn
            self.update()
            return

        if self.hot_seat:
            self.turn = turn
            self.update()
            return

        if turn != self.turn:
            self.hex_dictionary = \
                random_computer_turn(self.hex_dictionary, turn)
            self.win = is_winner(self.hex_dictionary, turn, self.rang)
            self.update()

        # print(self.hex_dictionary)
