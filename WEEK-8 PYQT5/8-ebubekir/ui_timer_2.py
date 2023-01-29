# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dell\OneDrive\Masaüstü\pyqt5\3 timer\timer2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(249, 281)
        about.setStyleSheet("background-color: rgb(174, 174, 255);")
        self.pushButton = QtWidgets.QPushButton(about)
        self.pushButton.setGeometry(QtCore.QRect(70, 220, 61, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(about)
        self.textEdit.setGeometry(QtCore.QRect(40, 50, 131, 141))
        self.textEdit.setStyleSheet("background-color: rgb(231, 255, 207);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(about)
        self.pushButton.clicked.connect(about.close)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About"))
        self.textEdit.setHtml(_translate("about", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Bu program ile</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">belirlediginiz bir </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">sureden</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">geri sayim </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">yapabilirsiniz.</span></p></body></html>"))

