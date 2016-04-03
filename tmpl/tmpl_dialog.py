# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

from dlgselectui import *

class DlgSelect(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.slt = Ui_Dialog()
        self.slt.setupUi(self)
        # Встановлюємо початкові значення

        # Приєднуємо слоти

        # Опрацювання сигналів

        return None

    def __del__ ( self ):
        self.ui = None
        return None


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     myapp = DlgSelect()
#     myapp.show()
#     sys.exit(app.exec_())