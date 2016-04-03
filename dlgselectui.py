# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiselect.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Select(object):
    def setupUi(self, Select):
        Select.setObjectName("Select")
        Select.resize(350, 250)
        Select.setMinimumSize(QtCore.QSize(350, 250))
        Select.setMaximumSize(QtCore.QSize(350, 250))
        self.btnBox = QtWidgets.QDialogButtonBox(Select)
        self.btnBox.setGeometry(QtCore.QRect(0, 210, 231, 32))
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setObjectName("btnBox")
        self.label = QtWidgets.QLabel(Select)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Select)
        self.label_2.setGeometry(QtCore.QRect(14, 60, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Select)
        self.label_3.setGeometry(QtCore.QRect(14, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Select)
        self.label_4.setGeometry(QtCore.QRect(14, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cbxTypeProd = QtWidgets.QComboBox(Select)
        self.cbxTypeProd.setGeometry(QtCore.QRect(137, 60, 201, 22))
        self.cbxTypeProd.setObjectName("cbxTypeProd")
        self.cbxPrepName = QtWidgets.QComboBox(Select)
        self.cbxPrepName.setGeometry(QtCore.QRect(137, 110, 201, 22))
        self.cbxPrepName.setObjectName("cbxPrepName")
        self.cbxSignName = QtWidgets.QComboBox(Select)
        self.cbxSignName.setGeometry(QtCore.QRect(137, 160, 201, 22))
        self.cbxSignName.setObjectName("cbxSignName")
        self.btnCansel = QtWidgets.QPushButton(Select)
        self.btnCansel.setGeometry(QtCore.QRect(263, 214, 75, 23))
        self.btnCansel.setObjectName("btnCansel")

        self.retranslateUi(Select)
        self.btnBox.accepted.connect(Select.accept)
        self.btnBox.rejected.connect(Select.reject)
        QtCore.QMetaObject.connectSlotsByName(Select)

    def retranslateUi(self, Select):
        _translate = QtCore.QCoreApplication.translate
        Select.setWindowTitle(_translate("Select", "Вибір препарату ..."))
        self.label.setText(_translate("Select", "Оберіть тип, препарат та показник для аналізу"))
        self.label_2.setText(_translate("Select", "Тип продукції"))
        self.label_3.setText(_translate("Select", "Назва препарату"))
        self.label_4.setText(_translate("Select", "Показник"))
        self.btnCansel.setText(_translate("Select", "Відміна"))

