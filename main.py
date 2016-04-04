# -*- coding: utf-8 -*-
__author__ = 'Valeriy'

import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPen
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

        # Приєднуємо слоти
        self.ui.btnSelectPrep.clicked.connect(self.openSelectPrep)
        self.ui.btnEditData.clicked.connect(self.openModifyData)
        self.ui.cmbYear.activated.connect(self.cmbSetYear)
        self.ui.btnAnlStart.clicked.connect(self.startAnl)
        self.ui.btnAnlStop.clicked.connect(self.stopAnl)
        self.ui.btnFilterStart.clicked.connect(self.startFilter)
        self.ui.btnFilterStop.clicked.connect(self.stopFilter)
        self.ui.btnPdf.clicked.connect(self.printPdf)
        self.ui.rdbReady.clicked.connect(self.setReady)
        self.ui.rdbIntermed.clicked.connect(self.setIntermed)
        # Встановлюємо початкові значення
        # прапорець режиму Фільтр
        self.flFilter = False
        self.flTypePrd = True
        self.selectYear()
        self.ui.cmbYear.setEnabled(False)
        self.ui.grbSelectType.setEnabled(False)
        self.idYear = self.ui.cmbYear.currentText()
        # Тимчасово виводио у лабел
        self.ui.lbYear.setText(self.idYear)
        self.model = QSqlTableModel()
        Data = (None, [])
        self.viewTable(Data, False)
        self.drawMap(Data,(0, 0))

        return None

    def __del__ ( self ):
        self.ui = None
        return None

# Опрацювання сигналів
    def openSelectPrep(self):
        self.idData = OpenDlgSelect()
        # print(self.idData[0], self.idData[1], self.idData[2], self.idData[3])
        self.ui.cmbYear.setEnabled(True)
        self.ui.grbSelectType.setEnabled(True)
        self.viewTable(self.idData, self.flFilter)
        fillData = self.getFillData(self.idData)
        dbData = self.getDataPrep(self.idData)
        print(dbData)
        self.fillVisuaData(self.idData, dbData, fillData, self.flFilter)
        self.clearDraw()
        self.drawMap(dbData,fillData)
        return None

    def cmbSetYear(self):
        self.idYear = self.ui.cmbYear.currentText()
        self.viewTable(self.idData, self.flFilter)
        dbData = self.getDataPrep(self.idData)
        fillData = self.getFillData(self.idData)
        self.fillVisuaData(self.idData, dbData, fillData, self.flFilter)
        self.clearDraw()
        self.drawMap(dbData, fillData)
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

        # Опрацювання gthtvbrfxf
    def setReady(self):
        self.flTypePrd = True
        dbData = self.getDataPrep(self.idData)
        fillData = self.getFillData(self.idData)
        self.fillVisuaData(self.idData, dbData, fillData, self.flFilter)
        self.clearDraw()
        self.drawMap(dbData, fillData)
        return None

    def setIntermed(self):
        self.flTypePrd = False
        dbData = self.getDataPrep(self.idData)
        fillData = self.getFillData(self.idData)
        self.fillVisuaData(self.idData, dbData, fillData, self.flFilter)
        self.clearDraw()
        self.drawMap(dbData, fillData)
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


    # *********************************************************
    def selectYear(self):
        strYear = dBase.queryGetYear()
        self.ui.cmbYear.addItems(strYear)
        return None

    def getDataPrep(self, idData):
        '''
        param: iDdata[0] Id препарата, iDdata[1] Id показника, iDdata[3] назва препарата, iDdata[4] назва показика]
        return: dataPrep[0] - кількысть даних, dataPrep[1] дані:
        '''
        if ((idData[0] != '') and (idData[1] != '')):
            dataPrep = dBase.queryGetDataPrep(idData[0], idData[1], self.idYear, self.flTypePrd)
        else:
            dataPrep[0] = []
            dataPrep[1] = []
        return dataPrep

    def getFillData(self, idData):
        '''
        :return SMax, SMin, OnlyReady, верхня межа, нижня межа, тип готова, проміжна:
        '''
        self.ui.grbSelectType.setEnabled(True)
        Data = dBase.queryGetDataSign(idData[0], idData[1])
        if Data[2]:
            self.ui.rdbReady = True
            self.ui.rdbIntermed = False
            self.ui.grbSelectType.setEnabled(False)
            self.flTypePrd = True
        return Data

    def fillVisuaData(self, idData, dbData, fillData, flFilter):
        '''
        idData[0] Id препарата; idData[1] Id показника; idData[2]; назва препарата; idData[3] назва показика]
        '''
        print('fillVisuaData')
        # fillData = dBase.queryGetDataSign(idData[0], idData[1])
        self.ui.lblPrepName.setText("Препарат: " + "<b>"+idData[2]+"</b>")
        self.ui.lblSignName.setText("Показник: " + "<b>"+idData[3]+"</b>")

        if (fillData[0] > 0):
            self.ui.lblMaxLimit.setText("Верхня межа: "+"<b>"+str('{0:.4f}'.format(fillData[0]))+"</b>")
        else:
            self.ui.lblAvg.setText("Верхня межа:")
        if (fillData[1] > 0):
            self.ui.lblMinLimit.setText("Нижня межа: "+"<b>"+str('{0:.4f}'.format(fillData[1]))+"</b>")
        else:
            self.ui.lblAvg.setText("Нижня межа:")

        self.ui.lblCount.setText("Кількість: "+"<b>"+str('{0}'.format(dbData[0]))+"</b>")

        if dbData[0] > 1:
            mathData = self.calcData(dbData)
        else:
            mathData = [None, None]

        if (mathData[0]) != None:
            self.ui.lblAvg.setText("Середнє значення: "+"<b>"+str('{0:.4f}'.format(mathData[0]))+"</b>")
        else:
            self.ui.lblAvg.setText("Середнє значення:")
        if (mathData[1]) != None:
            self.ui.lblStd.setText("Стандартне відхилення (sigma): "+"<b>"+str('{0:.4f}'.format(mathData[1]))+"</b>")
        else:
            self.ui.lblStd.setText("Стандартне відхилення (sigma):")
        return None

    def calcData(self, dbData):
        print("Dialog")
        if (dbData[1] != []):
            avgData = mean(dbData[1])
            stdData = stdev(dbData[1])
        else:
            avgData = None
            stdData = None
        return (avgData, stdData)

    def viewTable(self, idData, flFilter):
        print("viewTable")
        # print(idData[0], ' ', idData[1],' ', self.idYear, flFilter)
        # Налаштовуємо роботу з таблицею
        self.model.setTable('Pdata')
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        # Встановлюємо фільтри для виведення даних у таблицю
        self.model.setFilter("((PNameId="+str(idData[0])+") AND (SNameId="+str(idData[1])+") AND (YearId='"+str(self.idYear)+"'))")
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

    def drawMap(self, dbData, flData):
        statData = self.calcData(dbData)
        avgData = statData[0]
        stdData = statData[1]
        countData = len(dbData[1])
        maxData = flData[0]
        minData = flData[1]

        self.plot.autoFillBackground()
        self.plot.setTitle("A Simple Map Demonstration")
        self.plot.setCanvasBackground(Qt.white)
        self.plot.setAxisTitle(QwtPlot.xBottom, "серії")
        self.plot.setAxisTitle(QwtPlot.yLeft, "")

        # if (dbData[1] != []):

        # self.plot.setAxisScale(QwtPlot.xBottom, 0.0, 1.0)
        if ((minData != 0) and (maxData != 0)):
            cfScale = 0.01
            yScaleMin = minData - minData*cfScale
            yScaleMax = maxData + maxData*cfScale
            self.plot.setAxisScale(QwtPlot.yLeft, yScaleMin, yScaleMax)

    # Готуємо  графіки для виводу
        self.cMax = QwtPlotCurve()
        self.cMax.setPen(QPen(Qt.red))
        self.cMax.attach(self.plot)

        self.cMin = QwtPlotCurve()
        self.cMin.setPen(QPen(Qt.red))
        self.cMin.attach(self.plot)

        self.cMap = QwtPlotCurve()
        self.cMap.setPen(QPen(Qt.black))
        self.cMap.attach(self.plot)

        self.cAvg = QwtPlotCurve()
        self.cAvg.setPen(QPen(Qt.darkBlue))
        self.cAvg.attach(self.plot)

        self.c3SigmaP = QwtPlotCurve()
        self.c3SigmaP.setPen(QPen(Qt.green))
        self.c3SigmaP.attach(self.plot)
        self.c3SigmaN = QwtPlotCurve()
        self.c3SigmaN.setPen(QPen(Qt.green))
        self.c3SigmaN.attach(self.plot)

        self.c2SigmaP = QwtPlotCurve()
        self.c2SigmaP.setPen(QPen(Qt.blue))
        self.c2SigmaP.attach(self.plot)
        self.c2SigmaN = QwtPlotCurve()
        self.c2SigmaN.setPen(QPen(Qt.blue))
        self.c2SigmaN.attach(self.plot)


    # готуємо дані для виводу
        xData = np.arange(0, countData, 1)
    # лінія max, min границь препарату
        yMaxData = [maxData]*countData
        self.cMax.setData(xData, yMaxData)
        yMinData = [minData]*countData
        self.cMin.setData(xData, yMinData)
    # карта Шугарта
        yDataMap = dbData[1]
        self.cMap.setData(xData, yDataMap)
    # лінія середнього значення
        yAvgData = [avgData]*countData
        self.cAvg.setData(xData, yAvgData)
    # лінії 3 sigma значення
        y3SigmaP = None
        y3SigmaN = None
        y2SigmaP = None
        y2SigmaN = None
        if stdData != None:
            y3SigmaP = [avgData + 3*stdData]*countData
            y3SigmaN = [avgData - 3*stdData]*countData
            y2SigmaP = [avgData + 2*stdData]*countData
            y2SigmaN = [avgData - 2*stdData]*countData
        self.c3SigmaP.setData(xData, y3SigmaP)
        self.c3SigmaN.setData(xData, y3SigmaN)
        self.c2SigmaP.setData(xData, y2SigmaP)
        self.c2SigmaN.setData(xData, y2SigmaN)


        self.plot.replot()
        # self.plot.show()
        return None

    def clearDraw(self):
        self.cMap.detach()
        self.cAvg.detach()
        self.c3SigmaP.detach()
        self.c3SigmaN.detach()
        self.c2SigmaP.detach()
        self.c2SigmaN.detach()
        self.cMax.detach()
        self.cMin.detach()
        self.plot.replot()
        return None

    # *************Перевизначення подій ***********************
    def resizeEvent(self, event):
        # self.ui.textBrowser.repaint()
        rect = self.ui.plotwidget.frameSize()
        self.plot.resize(rect)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.showMaximized()
    # myapp.show()
    sys.exit(app.exec_())
