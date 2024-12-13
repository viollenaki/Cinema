# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMovie.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Adding(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        font = QtGui.QFont()
        font.setPointSize(7)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 20, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 122, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(8, 219, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setGeometry(QtCore.QRect(86, 324, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.apply.setFont(font)
        self.apply.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.apply.setObjectName("apply")
        self.title_text = QtWidgets.QLineEdit(Dialog)
        self.title_text.setGeometry(QtCore.QRect(146, 20, 146, 33))
        self.title_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.title_text.setObjectName("title_text")
        self.date_text = QtWidgets.QLineEdit(Dialog)
        self.date_text.setGeometry(QtCore.QRect(146, 122, 146, 33))
        self.date_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.date_text.setObjectName("date_text")
        self.price_text = QtWidgets.QLineEdit(Dialog)
        self.price_text.setGeometry(QtCore.QRect(146, 219, 146, 33))
        self.price_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.price_text.setObjectName("price_text")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Movie (Admin)"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Date</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Price</span></p></body></html>"))
        self.apply.setText(_translate("Dialog", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
