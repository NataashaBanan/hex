from PyQt5.QtWidgets import QApplication
import sys

from app.menu_widget import MenuWidget

app = QApplication(sys.argv)

v = MenuWidget()

v.show()
app.exec_()
