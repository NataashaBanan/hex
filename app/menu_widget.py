from PyQt5.QtWidgets import QWidget, QPushButton, QLCDNumber,\
    QSlider, QCheckBox, QLineEdit
from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtCore import Qt, QPoint

from app.menu_items import MenuItems
from app.game import Game
from app.paint_field import paint_field
from app.records import add_new_record, print_records
from app.difficulty import Difficulty
from app.save_game import save, print_saves, get_saves, load


def init_button(self, name, x0, y0, width, height, font):
    button = QPushButton(name, self)
    button.setFont(font)
    button.move(x0, y0)
    button.resize(width, height)
    button.autoFillBackground()

    return button


class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(30)

        self.menu_item = MenuItems.Menu

        self.width = 900
        self.height = 700
        self.setFixedSize(self.width, self.height)

        self.setWindowTitle('Hexxx')
        self.load_sld_value = 0
        self.blue_first_turn = False

        self.game_button = init_button(self, 'Game', 300, 50, 300, 100, font)
        self.settings_button = \
            init_button(self, 'Settings', 300, 200, 300, 100, font)
        self.records_button = \
            init_button(self, 'Records', 300, 350, 300, 100, font)
        self.load_btn = init_button(self, 'Load', 300, 500, 300, 100, font)
        font.setPointSize(20)
        self.back_to_menu_btn = \
            init_button(self, 'Menu', 50, 50, 100, 50, font)
        self.new_game_btn = \
            init_button(self, 'New game', 600, 300, 200, 100, font)
        self.undo_button = init_button(self, 'UNDO', 600, 200, 200, 100, font)
        self.redo_button = init_button(self, 'REDO', 600, 350, 200, 100, font)
        self.save_button = init_button(self, 'Save', 600, 500, 200, 100, font)

        font.setPointSize(40)

        self.lcd = QLCDNumber(self)
        self.hot_seat_cb = QCheckBox('Hot seat', self)
        self.textbox = QLineEdit(self)
        self.ok_button = \
            init_button(self, 'Ok', 300, 400, 300, 100, font)
        self.rang_sld = QSlider(Qt.Horizontal, self)
        self.load_sld = QSlider(Qt.Horizontal, self)
        self.diff_cb = QCheckBox('Difficult', self)
        self.blue_cb = QCheckBox('Blue', self)
        self.init_widgets()

        self.game = Game()

    def init_widgets(self):

        font = QFont()
        font.setPointSize(40)

        self.lcd.setFixedSize(200, 100)
        self.lcd.smallDecimalPoint()
        self.lcd.move(300, 400)
        self.lcd.display(11)

        self.textbox.move(200, 250)
        self.textbox.resize(500, 100)
        self.textbox.setFont(font)

        self.rang_sld.setFocusPolicy(Qt.NoFocus)
        self.rang_sld.setFixedSize(300, 50)
        self.rang_sld.move(250, 550)
        self.rang_sld.setMinimum(2)
        self.rang_sld.setMaximum(20)
        self.rang_sld.setValue(11)
        self.rang_sld.valueChanged[int].connect(self.rang_sld_move)
        self.rang_sld.valueChanged.connect(self.lcd.display)

        self.load_sld.setFixedSize(300, 50)
        self.load_sld.move(250, 550)
        self.load_sld.setValue(0)
        self.load_sld.setMinimum(0)
        self.load_sld.setMaximum(0)
        self.load_sld.valueChanged[int].connect(self.load_sld_move)

        self.diff_cb.setFont(font)
        self.diff_cb.move(300, 200)
        self.diff_cb.setStyleSheet(
            "QCheckBox::indicator { width:18px; height: 36px; }")

        self.blue_cb.setFont(font)
        self.blue_cb.move(325, 300)
        self.blue_cb. \
            setStyleSheet("QCheckBox::indicator { width:18px; height: 36px; }")

        self.hot_seat_cb.setFont(font)
        self.hot_seat_cb.move(325, 200)
        self.hot_seat_cb.\
            setStyleSheet("QCheckBox::indicator { width:18px; height: 36px; }")
        # cb.toggle()

        self.hot_seat_cb.stateChanged.connect(self.tick_hot_seat_cb)
        self.diff_cb.stateChanged.connect(self.tick_diff_cb)
        self.game_button.clicked.connect(self.game_button_clicked)
        self.settings_button.clicked.connect(self.settings_button_clicked)
        self.records_button.clicked.connect(self.records_button_clicked)
        self.back_to_menu_btn.clicked.connect(self.menu_button_clicked)
        self.ok_button.clicked.connect(self.ok_button_clicked)
        self.new_game_btn.clicked.connect(self.new_game_btn_clicked)
        self.redo_button.clicked.connect(self.redo_btn_clicked)
        self.undo_button.clicked.connect(self.undo_btn_clicked)
        self.save_button.clicked.connect(self.save_btn_clicked)
        self.load_btn.clicked.connect(self.load_btn_clicked)
        self.blue_cb.stateChanged.connect(self.tick_blue_cb)

        self.menu_button_clicked()

    def mousePressEvent(self, event):
        x = QPoint(event.pos()).x()
        y = QPoint(event.pos()).y()

        self.game.update_game(x, y)

        self.repaint()

    def tick_hot_seat_cb(self, state):
        if state == Qt.Checked:
            self.game.hot_seat = True
        else:
            self.game.hot_seat = False

    def tick_blue_cb(self, state):
        if state == Qt.Checked:
            self.blue_first_turn = True
        else:
            self.blue_first_turn = False

    def load_sld_move(self, value):
        self.load_sld_value = value

        self.repaint()

    def rang_sld_move(self, value):
        self.game.new_rang(value)

        self.repaint()

    def tick_diff_cb(self, state):
        if state == Qt.Checked:
            self.game.difficult = Difficulty.hard
        else:
            self.game.difficult = Difficulty.easy

    def new_game_btn_clicked(self):
        self.game.new_game()

        self.repaint()

    def undo_btn_clicked(self):
        self.game.undo()
        self.repaint()

    def redo_btn_clicked(self):
        self.game.redo()
        self.repaint()

    def ok_button_clicked(self):
        # self.ok_button.hide()

        if self.menu_item == MenuItems.Load:
            load(self.game, self.load_sld_value)
            self.menu_item = MenuItems.Game
            self.hide_all()
            self.back_to_menu_btn.show()
            self.undo_button.show()
            self.redo_button.show()
            self.save_button.show()

            self.repaint()

        elif self.menu_item == MenuItems.Save:
            text = self.textbox.text()
            self.textbox.setText("")
            save(text, self.game)

            self.menu_button_clicked()

        elif self.menu_item == MenuItems.HotSeat:
            self.hot_seat_cb.hide()
            self.blue_cb.hide()
            self.ok_button.hide()
            self.menu_item = MenuItems.Game
            self.back_to_menu_btn.show()
            self.undo_button.show()
            self.redo_button.show()
            self.save_button.show()
            if self.blue_first_turn:
                if not self.game.hot_seat:
                    self.game.first_computer_turn()
                else:
                    self.game.turn.another_turn()

            self.repaint()

        else:
            text = self.textbox.text()
            if text == "":
                return
            self.textbox.setText("")
            add_new_record(text)

            self.menu_button_clicked()

    def menu_button_clicked(self):
        self.menu_item = MenuItems.Menu

        self.hide_all()

        self.game_button.show()
        self.records_button.show()
        self.settings_button.show()
        self.load_btn.show()

        self.repaint()

    def load_btn_clicked(self):
        self.menu_item = MenuItems.Load
        self.hide_all()

        self.load_sld.setMaximum(max(len(get_saves()) - 1, 0))
        self.load_sld.show()

        self.back_to_menu_btn.show()
        self.ok_button.show()

        self.repaint()

    def add_new_record(self, painter):
        self.hide_all()
        painter.drawText(100, 150, str(self.game.turn) + " win!")
        painter.drawText(100, 200, "Congratulations,\n print your name please")

        self.textbox.show()
        self.ok_button.show()
        self.repaint()

    def save_btn_clicked(self):
        self.menu_item = MenuItems.Save

        self.hide_all()

        self.textbox.show()
        self.ok_button.show()

        self.repaint()

    def paintEvent(self, event):
        if self.menu_item == MenuItems.Menu:
            return

        if self.menu_item == MenuItems.Settings:
            return

        if self.menu_item == MenuItems.HotSeat:
            return

        painter = QPainter()
        painter.begin(self)
        font = QFont()
        font.setPointSize(30)

        painter.setFont(font)

        if self.menu_item == MenuItems.Load:
            print_saves(painter, self.load_sld_value)

        elif self.menu_item == MenuItems.Records:
            print_records(painter)

        elif self.game.newRecord:
            self.game.newRecord = False
            self.add_new_record(painter)

        elif self.game.win:
            painter.drawText(150, 150, str(self.game.turn) + " win!")

        elif self.menu_item == MenuItems.Game:
            paint_field(painter, self.game)
            painter.drawText(615, 150, "Turn " + str(self.game.turn))
        painter.end()

    def game_button_clicked(self):
        self.menu_item = MenuItems.HotSeat

        self.hide_all()

        self.hot_seat_cb.show()
        self.blue_cb.show()
        self.ok_button.show()

        self.game.new_game()

        self.repaint()

    def settings_button_clicked(self):
        self.menu_item = MenuItems.Settings

        self.hide_all()

        self.diff_cb.show()

        self.back_to_menu_btn.show()

        self.rang_sld.show()
        self.lcd.show()

        self.repaint()

    def records_button_clicked(self):
        self.menu_item = MenuItems.Records

        self.hide_all()

        self.back_to_menu_btn.show()

        self.repaint()

    def hide_all(self):
        self.new_game_btn.hide()
        self.back_to_menu_btn.hide()
        self.game_button.hide()
        self.records_button .hide()
        self.settings_button.hide()
        self.lcd.hide()
        self.rang_sld.hide()
        self.hot_seat_cb.hide()
        self.ok_button.hide()
        self.textbox.hide()
        self.diff_cb.hide()
        self.redo_button.hide()
        self.undo_button.hide()
        self.save_button.hide()
        self.load_btn.hide()
        self.load_sld.hide()
        self.blue_cb.hide()
