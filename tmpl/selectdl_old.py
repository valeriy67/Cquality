# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

from dlgselectui import *
from dbase import *

class DlgSelect(QtWidgets.QDialog):
    def __init__(self, parent=None):
        strTypeId = ''
        strNameId = ''
        strSignId = ''

        # self.resultId = ()
        QtWidgets.QDialog.__init__(self, parent)
        self.slct = Ui_Select()
        self.slct.setupUi(self)
        # Встановлюємо початкові значення
        self.dBase = DbData()
        self.strType = self.dBase.queryTypeProd()
        self.slct.cbxTypeProd.addItems(self.strType)
        # Приєднуємо слоти
        self.slct.cbxTypeProd.activated.connect(self.chnTypeProd)
        self.slct.cbxPrepName.activated.connect(self.chnNamePrep)
        self.slct.cbxSignName.activated.connect(self.chnSignPrep)
        return None

    def __del__ ( self ):
        self.dBase.con.close()
        self.dBase = None
        # self.ui.close()
        return None

    # Опрацювання сигналів
    def chnTypeProd(self):
        str = self.slct.cbxTypeProd.currentText()
        strName = self.dBase.queryNamePrep(str)
        self.slct.cbxPrepName.clear()
        self.slct.cbxPrepName.addItems(strName)
        self.slct.cbxPrepName.setEditable(True)
        self.strNameId = strName
        strName.clear()
        return None

    def chnNamePrep(self):
        str = self.slct.cbxPrepName.currentText()
        strName = self.dBase.queryNameSign(str)
        self.slct.cbxSignName.clear()
        self.slct.cbxSignName.addItems(strName)
        self.slct.cbxSignName.setEditable(True)
        return None

    def chnSignPrep(self):
        strName = self.slct.cbxPrepName.currentText()
        strSign = self.slct.cbxSignName.currentText()
        self.resultId = self.dBase.queryIdPrepSing(strName, strSign)
        print(self.resultId)
        return None


def OpenDlgSelect():
    ui = DlgSelect()
    result = ui.exec_()
    if result == ui.Accepted:
        tempData = ui.resultId
        ui.dBase.con.close()
        ui.close()
        return tempData
    else:
        ui.close()
        return None

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = DlgSelect()
    myapp.show()
    sys.exit(app.exec_())
