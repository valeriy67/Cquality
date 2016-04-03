# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

import sys

# from PyQt5 import QtWidgets

from PyQt5.QtGui import QIcon


from interface import *

# Номер збірки

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QIcon('pic/favicon.ico'))
        self.ui = Ui_Main()
        self.ui.setupUi(self)

    # Встановлюємо початкові значення

    # Приєднуємо слоти
    # Опрацювання сигналів

        return None

    def __del__ ( self ):
        self.ui = None
        return None




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
