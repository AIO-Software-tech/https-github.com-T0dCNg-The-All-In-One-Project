# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ogban\Desktop\The-All-In-One-Project\The-All-In-One-Project\AIO Gui\Countdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 250)
        MainWindow.setMinimumSize(QtCore.QSize(488, 250))
        MainWindow.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(46)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(230, 200, 85);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Close.setFont(font)
        self.Close.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.Close.setAutoDefault(False)
        self.Close.setDefault(False)
        self.Close.setObjectName("Close")
        self.gridLayout.addWidget(self.Close, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.countdown = QtWidgets.QLineEdit(self.centralwidget)
        self.countdown.setMinimumSize(QtCore.QSize(0, 85))
        self.countdown.setReadOnly(True)
        self.countdown.setObjectName("countdown")
        self.gridLayout.addWidget(self.countdown, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Please Wait</p></body></html>"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.label_3.setText(_translate("MainWindow", "AIO \"GUI Edittion\" | Version: v-2.1.0 REV-2 | GUI Version:Alpha 0.0.1 | Copyright AIO 2022"))
