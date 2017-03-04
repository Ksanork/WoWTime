# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\status_dialog_1.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatusDialog1(object):
    def setupUi(self, StatusDialog1):
        StatusDialog1.setObjectName("StatusDialog1")
        StatusDialog1.resize(204, 144)
        self.label = QtWidgets.QLabel(StatusDialog1)
        self.label.setGeometry(QtCore.QRect(0, 0, 204, 144))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/bg.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StatusDialog1)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 62, 23))
        font = QtGui.QFont()
        font.setFamily("Trajan Pro 3")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(StatusDialog1)
        self.label_3.setGeometry(QtCore.QRect(90, 50, 102, 20))
        font = QtGui.QFont()
        font.setFamily("Trajan Pro")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(68, 206, 0);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(StatusDialog1)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog1)

    def retranslateUi(self, StatusDialog1):
        _translate = QtCore.QCoreApplication.translate
        StatusDialog1.setWindowTitle(_translate("StatusDialog1", "Dialog"))
        self.label_2.setText(_translate("StatusDialog1", "Status:"))
        self.label_3.setText(_translate("StatusDialog1", "Wyłączony"))

