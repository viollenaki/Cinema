# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Info2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(8, 104, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.movie_list_2 = QtWidgets.QListWidget(Dialog)
        self.movie_list_2.setGeometry(QtCore.QRect(8, 151, 284, 240))
        self.movie_list_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.movie_list_2.setObjectName("movie_list_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 57, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 9, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.title_text = QtWidgets.QLineEdit(Dialog)
        self.title_text.setGeometry(QtCore.QRect(146, 9, 146, 33))
        self.title_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.title_text.setObjectName("title_text")
        self.seance_text = QtWidgets.QLineEdit(Dialog)
        self.seance_text.setGeometry(QtCore.QRect(146, 57, 146, 33))
        self.seance_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.seance_text.setObjectName("seance_text")
        self.people_text = QtWidgets.QLineEdit(Dialog)
        self.people_text.setGeometry(QtCore.QRect(146, 104, 146, 33))
        self.people_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.people_text.setObjectName("people_text")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Total Info"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">People</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Seance</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
