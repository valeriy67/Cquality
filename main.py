# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from interface import *
from dlgselect import *
from dlgmodifyui import *
from statistics import *

from qwt import QwtPlot, QwtPlotCurve
import numpy as np

# Номер збірки
numBuild = '01_220216'


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QIcon('pic/favicon.ico'))
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        # Додаємо widget  QwtPlot для побудови графіків
        self.plot = QwtPlot(self.ui.plotwidget)

        # Встановлюємо початкові значення
        self.selectYear()
        self.ui.cmbYear.setEnabled(False)
        self.idYear = self.ui.cmbYear.currentText()
        # Тимчасово виводио у лабел
        self.ui.lbYear.setText(self.idYear)
        self.model = QSqlTableModel()

        self.ui.plotwidget.setAutoFillBackground(True)



        # Приєднуємо слоти
        self.ui.btnSelectPrep.clicked.connect(self.openSelectPrep)
        self.ui.btnEditData.clicked.connect(self.openModifyData)
        self.ui.cmbYear.activated.connect(self.cmbSetYear)

        self.ui.btnAnlStart.clicked.connect(self.startAnl)
        self.ui.btnAnlStop.clicked.connect(self.stopAnl)

        self.ui.btnFilterStart.clicked.connect(self.startFilter)
        self.ui.btnFilterStop.clicked.connect(self.stopFilter)
        self.ui.btnPdf.clicked.connect(self.printPdf)

        self.viewTable(None, None, self.idYear)
        self.drawMap('', '', None)

        return None

    def __del__ ( self ):
        self.ui = None
        return None

# Опрацювання сигналів
    def openSelectPrep(self):
        self.idData = OpenDlgSelect()
        self.clearDraw()

        if (self.idData != None):
            self.ui.cmbYear.setEnabled(True)
            self.viewTable(self.idData[0], self.idData[1], self.idYear)
            self.drawMap(self.idData[0], self.idData[1], self.idYear)
            self.fillVisuaData(self.idData)
        return None

    def cmbSetYear(self):
        self.idYear = self.ui.cmbYear.currentText()
        self.clearDraw()
        if (self.idData != None):
            self.viewTable(self.idData[0], self.idData[1], self.idYear)
            self.drawMap(self.idData[0], self.idData[1], self.idYear)
            self.fillVisuaData(self.idData)
        return None

    def openModifyData(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Modify()
        ui.setupUi(Dialog)
        Dialog.exec()
        Dialog.close()
        # Якщо змінили дані перерисувати графік і таблицю
        # self.clearDraw()
        return None

    def startAnl(self):
        pass

    def stopAnl(self):
        pass

    def startFilter(self):
        pass

    def stopFilter(self):
        pass

    def printPdf(self):
        pass
# *********** Звершення опису функцій опрацювання сигналів *************


    # *************Перевизначення подій ***********************

    def resizeEvent(self, event):
        # self.ui.textBrowser.repaint()
        rect = self.ui.plotwidget.frameSize()
        self.plot.resize(rect)

    # *********************************************************

    def fillVisuaData(self, idData):
        '''
        iDdata[0] Id препарата, iDdata[1] Id показника, iDdata[3] назва препарата, iDdata[4] назва показика]
        '''
        # self.ui.lblPrepName.clear()
        self.ui.lblPrepName.setText("Препарат: " + "<b>"+idData[2]+"</b>")
        # self.ui.lblSignName.clear()
        self.ui.lblSignName.setText("Показник: " + "<b>"+idData[3]+"</b>")
        # self.ui.lblMaxLimit =
        # self.ui.lblMinLimit =
        mathData = self.calcData(idData, self.idYear)
        if (mathData[0]) != None:
            self.ui.lblAvg.setText("Середнє значення: "+"<b>"+str('{0:.4f}'.format(mathData[0]))+"</b>")
        else:
            self.ui.lblAvg.setText("Середнє значення:")
        if (mathData[1]) != None:
            self.ui.lblStd.setText("Стандартне відхилення (sigma): "+"<b>"+str('{0:.4f}'.format(mathData[1]))+"</b>")
        else:
            self.ui.lblStd.setText("Стандартне відхилення (sigma):")


        # self.ui.lblAvg.setText("Середнє значення: " + str('{0:.4f}'.format(x)))
        # self.ui.lblStd.setText("Стандартне відхилення (sigma): " + "'{0:.4f}'".format(str(mathData[1])))

    def calcData(self, iDdata, yearId):
        dataPrep = dBase.queryGetDataPrep(iDdata[0], iDdata[1], yearId)
        if (dataPrep[1] != []):
            avgData = mean(dataPrep[1])
            stdData = stdev(dataPrep[1])
        else:
            avgData = None
            stdData = None

        return (avgData, stdData)

    def selectYear(self):
        strYear = dBase.queryGetYear()
        self.ui.cmbYear.addItems(strYear)

        return None

    def drawMap(self, nameId, signId, yearId):
        print('drawMap')
        print(nameId, ' ', signId,' ', yearId)
        if ((nameId != '') and (signId != '') and (yearId !=0)):
            dataPrep = dBase.queryGetDataPrep(nameId, signId, yearId)
            x = np.arange(1, dataPrep[0])
            y = dataPrep[1]
        else:
            x = []
            y = []
        self.plot.autoFillBackground()
        self.plot.setTitle("A Simple Map Demonstration")
        self.plot.setCanvasBackground(Qt.white)
        self.plot.setAxisTitle(QwtPlot.xBottom, "серії")
        # self.plot.setAxisTitle(QwtPlot.yLeft, "y")
        # self.plot.setAxisScale(QwtPlot.xBottom, 0.0, 1.0)
        # self.plot.setAxisScale(QwtPlot.yLeft, 0.54, 0.56)
        self.curve = QwtPlotCurve()
        self.curve.setData(x, y)
        self.curve.attach(self.plot)
        self.plot.replot()
        # self.plot.show()

        return None

    def clearDraw(self):
        self.curve.detach()
        self.plot.replot()
        return None

    def viewTable(self, idPrep, idSign, idYear):
        print("viewTable")
        print(idPrep, ' ', idSign,' ', idYear)
        # Налаштовуємо роботу з таблицею
        self.model.setTable('Pdata')
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        # Встановлюємо фільтри для виведення даних у таблицю
        self.model.setFilter("((PNameId="+str(idPrep)+") AND (SNameId="+str(idSign)+") AND (YearId='"+str(idYear)+"'))")
        self.ui.DataTable.setModel(self.model)

        # Встановлюємо заголовки таблиці
        self.model.setHeaderData(3, Qt.Horizontal, "Серія")
        self.model.setHeaderData(4, Qt.Horizontal, "Проміжна")
        self.model.setHeaderData(5, Qt.Horizontal, "Готова")
        # Встановлюємо ширину колонок таблиці
        self.ui.DataTable.setColumnWidth(3, 80)
        self.ui.DataTable.setColumnWidth(4, 80)
        self.ui.DataTable.setColumnWidth(5, 80)
        # Приховуємо зайві колонки (поля бази даних)
        self.ui.DataTable.hideColumn(0)
        self.ui.DataTable.hideColumn(1)
        self.ui.DataTable.hideColumn(2)
        self.ui.DataTable.hideColumn(6)
        self.ui.DataTable.hideColumn(7)
        self.ui.DataTable.hideColumn(8)
        self.ui.DataTable.hideColumn(9)
        self.ui.DataTable.hideColumn(10)
        self.ui.DataTable.show()
        return None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.showMaximized()
    # myapp.show()
    sys.exit(app.exec_())
