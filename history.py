# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 513)
        Form.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 121, 71))
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"font-size: 20px;\n"
"border-radius: 10px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 121, 71))
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"font-size: 20px;\n"
"border-radius: 10px")
        self.label_2.setObjectName("label_2")
        self.movies_list = QtWidgets.QListWidget(Form)
        self.movies_list.setGeometry(QtCore.QRect(40, 150, 191, 192))
        self.movies_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"")
        self.movies_list.setObjectName("movies_list")
        self.seances_list = QtWidgets.QListWidget(Form)
        self.seances_list.setGeometry(QtCore.QRect(300, 150, 191, 192))
        self.seances_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"")
        self.seances_list.setObjectName("seances_list")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">movies</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">date</p></body></html>"))
