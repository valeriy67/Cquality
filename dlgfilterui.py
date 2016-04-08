# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\uifilter.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Filter(object):
    def setupUi(self, Filter):
        Filter.setObjectName("Filter")
        Filter.resize(350, 200)
        Filter.setMinimumSize(QtCore.QSize(350, 200))
        Filter.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        Filter.setFont(font)
        self.label = QtWidgets.QLabel(Filter)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Filter)
        self.label_2.setGeometry(QtCore.QRect(16, 60, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Filter)
        self.label_3.setGeometry(QtCore.QRect(16, 102, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Filter)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 331, 41))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.btnOk = QtWidgets.QPushButton(self.groupBox)
        self.btnOk.setGeometry(QtCore.QRect(160, 13, 75, 23))
        self.btnOk.setDefault(True)
        self.btnOk.setObjectName("btnOk")
        self.btnCancel = QtWidgets.QPushButton(self.groupBox)
        self.btnCancel.setGeometry(QtCore.QRect(250, 13, 75, 23))
        self.btnCancel.setObjectName("btnCancel")
        self.lineStart = QtWidgets.QLineEdit(Filter)
        self.lineStart.setGeometry(QtCore.QRect(126, 60, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineStart.setFont(font)
        self.lineStart.setObjectName("lineStart")
        self.lineEnd = QtWidgets.QLineEdit(Filter)
        self.lineEnd.setGeometry(QtCore.QRect(126, 100, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEnd.setFont(font)
        self.lineEnd.setObjectName("lineEnd")

        self.retranslateUi(Filter)
        QtCore.QMetaObject.connectSlotsByName(Filter)

    def retranslateUi(self, Filter):
        _translate = QtCore.QCoreApplication.translate
        Filter.setWindowTitle(_translate("Filter", "Фільтр ..."))
        self.label.setText(_translate("Filter", "Вкажіть межі серій для фільтрування"))
        self.label_2.setText(_translate("Filter", "Початок:"))
        self.label_3.setText(_translate("Filter", "Кінець:"))
        self.btnOk.setText(_translate("Filter", "Прийняти"))
        self.btnCancel.setText(_translate("Filter", "Відміна"))

