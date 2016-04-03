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
        # self.dBase = DbData()
        self.strType = dBase.queryTypeProd()
        self.slct.cbxTypeProd.addItems(self.strType)
        self.strType = self.slct.cbxTypeProd.currentText()
        self.slct.cbxTypeProd.setEditable(True)
        strName = dBase.queryNamePrep(self.strType)
        self.slct.cbxPrepName.clear()
        self.slct.cbxPrepName.addItems(strName)
        self.slct.cbxPrepName.setEditable(True)
        self.slct.cbxPrepName.setEditable(True)
        self.slct.btnBox.setEnabled(False)

        # Приєднуємо слоти
        self.slct.cbxTypeProd.activated.connect(self.chnTypeProd)
        self.slct.cbxPrepName.activated.connect(self.chnNamePrep)
        self.slct.cbxSignName.activated.connect(self.chnSignPrep)
        self.slct.btnCansel.clicked.connect(self.clickCansel)

        return None

    def __del__ ( self ):
        # dBase.con.close()
        # dBase = None
        # self.ui.close()
        return None

    # Опрацювання сигналів
    def clickCansel(self):
    # Переписати нормально
        result = self.Rejected
        self.close()
        return result

    def chnTypeProd(self):
        self.strType = self.slct.cbxTypeProd.currentText()
        strName = dBase.queryNamePrep(self.strType)
        self.slct.cbxPrepName.clear()
        self.slct.cbxPrepName.addItems(strName)
        self.slct.cbxPrepName.setEditable(True)
        # self.strNameId = strName
        # strName.clear()
        return None

    def chnNamePrep(self):
        self.strNamePrep = self.slct.cbxPrepName.currentText()
        strNameList = dBase.queryNameSign(self.strNamePrep)
        self.slct.cbxSignName.clear()
        self.slct.cbxSignName.addItems(strNameList)
        self.slct.cbxSignName.setEditable(True)
        return None

    def chnSignPrep(self):
        '''
        :return: індекс препарату, індекс показника, назву препарату, назву показника
        '''
        # strName = self.slct.cbxPrepName.currentText()
        self.strNameSign = self.slct.cbxSignName.currentText()
        # Отримуємо Id препарату і показника
        result = dBase.queryIdPrepSing(self.strNamePrep, self.strNameSign)
        self.results = (result[0], result[1], self.strNamePrep, self.strNameSign)
        if (self.strNameSign != ''):
            self.slct.btnBox.setEnabled(True)
        return None


def OpenDlgSelect():
    ui = DlgSelect()
    result = ui.exec_()
    if result == ui.Accepted:
        resData = ui.results
        # dBase.con.close()
        ui.close()
        return resData
    else:
        ui.close()
        return None

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = DlgSelect()
    myapp.show()
    sys.exit(app.exec_())
