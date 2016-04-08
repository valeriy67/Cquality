# -*- coding: utf-8 -*-
__author__ = 'Valeriy'


import sys
from dlgfilterui import *

class DlgFilter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # self.resultId = ()
        QtWidgets.QDialog.__init__(self, parent)
        self.fltr = Ui_Filter()
        self.fltr.setupUi(self)
        # Встановлюємо початкові значення
        self.fltr.btnOk.clicked.connect(self.accept)
        self.fltr.btnCancel.clicked.connect(self.reject)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = DlgFilter()
    myapp.show()
    sys.exit(app.exec_())