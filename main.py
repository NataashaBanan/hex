from PyQt5.QtWidgets import QApplication
import sys

from field_widget import FieldWidget

app = QApplication(sys.argv)

v = FieldWidget()

v.show()
app.exec_()
