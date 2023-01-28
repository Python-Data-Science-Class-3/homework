# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dell\OneDrive\Masaüstü\pyqt5\3 timer\timer3_setter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(251, 93)
        Dialog.setStyleSheet("background-color: rgb(187, 255, 224);")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 195, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox_settimer = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_settimer.setStyleSheet("background-color: rgb(255, 255, 199);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.spinBox_settimer.setObjectName("spinBox_settimer")
        self.verticalLayout.addWidget(self.spinBox_settimer)
        self.buttonBox_settimer = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox_settimer.setStyleSheet("background-color: rgb(255, 255, 151);")
        self.buttonBox_settimer.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_settimer.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_settimer.setObjectName("buttonBox_settimer")
        self.verticalLayout.addWidget(self.buttonBox_settimer)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "settimer"))

