# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        Main.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pic/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DataTable = QtWidgets.QTableView(self.centralwidget)
        self.DataTable.setMinimumSize(QtCore.QSize(260, 495))
        self.DataTable.setMaximumSize(QtCore.QSize(260, 16777215))
        self.DataTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DataTable.setObjectName("DataTable")
        self.DataTable.horizontalHeader().setMinimumSectionSize(25)
        self.DataTable.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.DataTable, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(180, 500))
        self.groupBox_2.setMaximumSize(QtCore.QSize(180, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblPrepName = QtWidgets.QLabel(self.groupBox_2)
        self.lblPrepName.setGeometry(QtCore.QRect(10, 19, 161, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPrepName.sizePolicy().hasHeightForWidth())
        self.lblPrepName.setSizePolicy(sizePolicy)
        self.lblPrepName.setMinimumSize(QtCore.QSize(161, 50))
        self.lblPrepName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblPrepName.setWordWrap(True)
        self.lblPrepName.setObjectName("lblPrepName")
        self.lblSignName = QtWidgets.QLabel(self.groupBox_2)
        self.lblSignName.setGeometry(QtCore.QRect(10, 79, 161, 50))
        self.lblSignName.setMinimumSize(QtCore.QSize(161, 50))
        self.lblSignName.setMaximumSize(QtCore.QSize(161, 61))
        self.lblSignName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblSignName.setWordWrap(True)
        self.lblSignName.setObjectName("lblSignName")
        self.lblMaxLimit = QtWidgets.QLabel(self.groupBox_2)
        self.lblMaxLimit.setGeometry(QtCore.QRect(10, 176, 161, 16))
        self.lblMaxLimit.setMinimumSize(QtCore.QSize(161, 16))
        self.lblMaxLimit.setMaximumSize(QtCore.QSize(161, 16))
        self.lblMaxLimit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblMaxLimit.setWordWrap(False)
        self.lblMaxLimit.setObjectName("lblMaxLimit")
        self.lblMinLimit = QtWidgets.QLabel(self.groupBox_2)
        self.lblMinLimit.setGeometry(QtCore.QRect(10, 206, 161, 16))
        self.lblMinLimit.setMinimumSize(QtCore.QSize(161, 16))
        self.lblMinLimit.setMaximumSize(QtCore.QSize(161, 16))
        self.lblMinLimit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblMinLimit.setWordWrap(False)
        self.lblMinLimit.setObjectName("lblMinLimit")
        self.lblStd = QtWidgets.QLabel(self.groupBox_2)
        self.lblStd.setGeometry(QtCore.QRect(10, 260, 161, 26))
        self.lblStd.setMinimumSize(QtCore.QSize(161, 26))
        self.lblStd.setMaximumSize(QtCore.QSize(161, 26))
        self.lblStd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblStd.setWordWrap(True)
        self.lblStd.setIndent(0)
        self.lblStd.setObjectName("lblStd")
        self.lblAvg = QtWidgets.QLabel(self.groupBox_2)
        self.lblAvg.setGeometry(QtCore.QRect(10, 230, 161, 16))
        self.lblAvg.setMinimumSize(QtCore.QSize(161, 16))
        self.lblAvg.setMaximumSize(QtCore.QSize(161, 16))
        self.lblAvg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblAvg.setWordWrap(False)
        self.lblAvg.setObjectName("lblAvg")
        self.lblCaption = QtWidgets.QLabel(self.groupBox_2)
        self.lblCaption.setGeometry(QtCore.QRect(10, 310, 161, 16))
        self.lblCaption.setMinimumSize(QtCore.QSize(161, 16))
        self.lblCaption.setMaximumSize(QtCore.QSize(161, 16))
        self.lblCaption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblCaption.setObjectName("lblCaption")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(2, 330, 175, 165))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(175, 165))
        self.textBrowser.setMaximumSize(QtCore.QSize(175, 16777215))
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setObjectName("textBrowser")
        self.lblCount = QtWidgets.QLabel(self.groupBox_2)
        self.lblCount.setGeometry(QtCore.QRect(10, 148, 161, 16))
        self.lblCount.setMinimumSize(QtCore.QSize(161, 16))
        self.lblCount.setMaximumSize(QtCore.QSize(161, 16))
        self.lblCount.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblCount.setWordWrap(False)
        self.lblCount.setObjectName("lblCount")
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.plotwidget = QtWidgets.QWidget(self.centralwidget)
        self.plotwidget.setMinimumSize(QtCore.QSize(335, 495))
        self.plotwidget.setObjectName("plotwidget")
        self.gridLayout.addWidget(self.plotwidget, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(780, 36))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 36))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.btnSelectPrep = QtWidgets.QPushButton(self.groupBox)
        self.btnSelectPrep.setGeometry(QtCore.QRect(10, 0, 36, 36))
        self.btnSelectPrep.setMinimumSize(QtCore.QSize(36, 36))
        self.btnSelectPrep.setMaximumSize(QtCore.QSize(36, 36))
        self.btnSelectPrep.setIconSize(QtCore.QSize(24, 24))
        self.btnSelectPrep.setObjectName("btnSelectPrep")
        self.btnEditData = QtWidgets.QPushButton(self.groupBox)
        self.btnEditData.setGeometry(QtCore.QRect(50, 0, 36, 36))
        self.btnEditData.setMinimumSize(QtCore.QSize(36, 36))
        self.btnEditData.setMaximumSize(QtCore.QSize(36, 36))
        self.btnEditData.setIconSize(QtCore.QSize(24, 24))
        self.btnEditData.setObjectName("btnEditData")
        self.cmbYear = QtWidgets.QComboBox(self.groupBox)
        self.cmbYear.setGeometry(QtCore.QRect(103, 2, 71, 31))
        self.cmbYear.setObjectName("cmbYear")
        self.grbSelectType = QtWidgets.QGroupBox(self.groupBox)
        self.grbSelectType.setEnabled(True)
        self.grbSelectType.setGeometry(QtCore.QRect(270, 3, 151, 30))
        self.grbSelectType.setTitle("")
        self.grbSelectType.setCheckable(False)
        self.grbSelectType.setObjectName("grbSelectType")
        self.rdbIntermed = QtWidgets.QRadioButton(self.grbSelectType)
        self.rdbIntermed.setGeometry(QtCore.QRect(6, 7, 71, 17))
        self.rdbIntermed.setChecked(False)
        self.rdbIntermed.setObjectName("rdbIntermed")
        self.rdbReady = QtWidgets.QRadioButton(self.grbSelectType)
        self.rdbReady.setGeometry(QtCore.QRect(81, 7, 61, 17))
        self.rdbReady.setChecked(True)
        self.rdbReady.setObjectName("rdbReady")
        self.btnAnlStart = QtWidgets.QPushButton(self.groupBox)
        self.btnAnlStart.setGeometry(QtCore.QRect(440, 0, 36, 36))
        self.btnAnlStart.setMinimumSize(QtCore.QSize(36, 36))
        self.btnAnlStart.setMaximumSize(QtCore.QSize(36, 36))
        self.btnAnlStart.setIconSize(QtCore.QSize(24, 24))
        self.btnAnlStart.setObjectName("btnAnlStart")
        self.btnAnlStop = QtWidgets.QPushButton(self.groupBox)
        self.btnAnlStop.setGeometry(QtCore.QRect(480, 0, 36, 36))
        self.btnAnlStop.setMinimumSize(QtCore.QSize(36, 36))
        self.btnAnlStop.setMaximumSize(QtCore.QSize(36, 36))
        self.btnAnlStop.setIconSize(QtCore.QSize(24, 24))
        self.btnAnlStop.setObjectName("btnAnlStop")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(190, 5, 71, 20))
        self.label_2.setObjectName("label_2")
        self.btnFilterStart = QtWidgets.QPushButton(self.groupBox)
        self.btnFilterStart.setGeometry(QtCore.QRect(530, 0, 36, 36))
        self.btnFilterStart.setMinimumSize(QtCore.QSize(36, 36))
        self.btnFilterStart.setMaximumSize(QtCore.QSize(36, 36))
        self.btnFilterStart.setIconSize(QtCore.QSize(24, 24))
        self.btnFilterStart.setObjectName("btnFilterStart")
        self.btnFilterStop = QtWidgets.QPushButton(self.groupBox)
        self.btnFilterStop.setGeometry(QtCore.QRect(570, 0, 36, 36))
        self.btnFilterStop.setMinimumSize(QtCore.QSize(36, 36))
        self.btnFilterStop.setMaximumSize(QtCore.QSize(36, 36))
        self.btnFilterStop.setIconSize(QtCore.QSize(24, 24))
        self.btnFilterStop.setObjectName("btnFilterStop")
        self.btnPdf = QtWidgets.QPushButton(self.groupBox)
        self.btnPdf.setGeometry(QtCore.QRect(621, 0, 36, 36))
        self.btnPdf.setMinimumSize(QtCore.QSize(36, 36))
        self.btnPdf.setMaximumSize(QtCore.QSize(36, 36))
        self.btnPdf.setIconSize(QtCore.QSize(24, 24))
        self.btnPdf.setObjectName("btnPdf")
        self.lbYear = QtWidgets.QLabel(self.groupBox)
        self.lbYear.setGeometry(QtCore.QRect(690, 10, 47, 13))
        self.lbYear.setObjectName("lbYear")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Main)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(Main)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(Main)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(Main)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)
        Main.setTabOrder(self.btnSelectPrep, self.btnEditData)
        Main.setTabOrder(self.btnEditData, self.cmbYear)
        Main.setTabOrder(self.cmbYear, self.rdbIntermed)
        Main.setTabOrder(self.rdbIntermed, self.rdbReady)
        Main.setTabOrder(self.rdbReady, self.btnAnlStart)
        Main.setTabOrder(self.btnAnlStart, self.btnAnlStop)
        Main.setTabOrder(self.btnAnlStop, self.DataTable)
        Main.setTabOrder(self.DataTable, self.textBrowser)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Cquality"))
        self.groupBox_2.setTitle(_translate("Main", "Показники"))
        self.lblPrepName.setText(_translate("Main", "Препарат:"))
        self.lblSignName.setText(_translate("Main", "Показник:"))
        self.lblMaxLimit.setText(_translate("Main", "Верхня межа:"))
        self.lblMinLimit.setText(_translate("Main", "Нижня межа:"))
        self.lblStd.setText(_translate("Main", "Стандартне відхилення (sigma):"))
        self.lblAvg.setText(_translate("Main", "Середнє значення:"))
        self.lblCaption.setText(_translate("Main", "Результат аналізу"))
        self.lblCount.setText(_translate("Main", "Кількість:"))
        self.btnSelectPrep.setText(_translate("Main", "Пр"))
        self.btnEditData.setText(_translate("Main", "Пр+"))
        self.rdbIntermed.setText(_translate("Main", "Проміжна"))
        self.rdbReady.setText(_translate("Main", "Готова"))
        self.btnAnlStart.setText(_translate("Main", "A+"))
        self.btnAnlStop.setText(_translate("Main", "A-"))
        self.label_2.setText(_translate("Main", "Тип продукції:"))
        self.btnFilterStart.setText(_translate("Main", "Ф+"))
        self.btnFilterStop.setText(_translate("Main", "Ф-"))
        self.btnPdf.setText(_translate("Main", "PDF"))
        self.lbYear.setText(_translate("Main", "РІК"))
        self.menu.setTitle(_translate("Main", "Довідник"))
        self.menu_2.setTitle(_translate("Main", "Вихід"))
        self.action.setText(_translate("Main", "Препарати"))
        self.action_2.setText(_translate("Main", "Показники"))
        self.action_3.setText(_translate("Main", "Користувачі"))
        self.action_4.setText(_translate("Main", "Рік"))

