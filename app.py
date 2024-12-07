import sys
import requests
import json

main_user = 'akbar'
main_password = '123'

users = set()

clients = {}
class Client:
    def __init__(self, name, password):
        self.name = name
        self.password = password



from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Registration(QtWidgets.QDialog):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.setWindowModality(QtCore.Qt.ApplicationModal)
        Registration.resize(300, 400)
        Registration.setStyleSheet("background-color:rgb(148, 143, 124)")

        # Создание меток
        self.label = QtWidgets.QLabel(Registration)
        self.label.setGeometry(QtCore.QRect(40, 10, 231, 31))
        self.label.setStyleSheet("background-color:rgb(15, 86, 90)")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Registration)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 231, 31))
        self.label_2.setStyleSheet("background-color:rgb(15, 86, 90)")
        self.label_2.setObjectName("label_2")
        
        # Поля ввода
        self.username = QtWidgets.QLineEdit(Registration)
        self.username.setGeometry(QtCore.QRect(60, 50, 191, 31))
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username.setObjectName("username")
        
        self.password = QtWidgets.QLineEdit(Registration)
        self.password.setGeometry(QtCore.QRect(60, 140, 191, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        
        self.confirm_password = QtWidgets.QLineEdit(Registration)
        self.confirm_password.setGeometry(QtCore.QRect(60, 230, 191, 31))
        self.confirm_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setObjectName("confirm_password")
        
        # Метка для подтверждения пароля
        self.label_3 = QtWidgets.QLabel(Registration)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 231, 31))
        self.label_3.setStyleSheet("background-color:rgb(15, 86, 90)")
        self.label_3.setObjectName("label_3")
        
        # Кнопка "Sign Up"
        self.sign_up = QtWidgets.QPushButton(Registration)
        self.sign_up.setGeometry(QtCore.QRect(40, 280, 231, 71))
        self.sign_up.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(15, 86, 90);\n"
                                   "font-size: 30px;\n")
        self.sign_up.setObjectName("sign_up")
 
         # Подключение действий
        self.sign_up.clicked.connect(self.sign_up_clicked)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration"))
        self.label.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff; border-radius: 20px;\">Username</span></p></body></html>"))
        self.label_2.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;border-radius: 20px; \">Password</span></p></body></html>"))
        self.label_3.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff; border-radius: 20px;\">Confirm Password</span></p></body></html>"))
        self.sign_up.setText(_translate("Registration", "Sign Up"))


    def sign_up_clicked(self):
        username = self.username.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if password == confirm_password:
            if username not in users:
                users.add(username)
                clients[username] = Client(username, password)

                QtWidgets.QMessageBox.information(self, "Success", "Registration successful.")
                self.accept()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Username already exists.")    
                
        else:
            # Ошибка, если пароли не совпадают
            QtWidgets.QMessageBox.critical(self, "Error", "Passwords do not match.")






class Ui_Login_Window(QtWidgets.QWidget):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(300, 400)
        Login_Window.setStyleSheet("background-color:rgb(148, 143, 124)")
        self.label = QtWidgets.QLabel(Login_Window)
        self.label.setGeometry(QtCore.QRect(60, 10, 191, 31))
        self.label.setStyleSheet("background-color:rgb(15, 86, 90)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login_Window)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 191, 31))
        self.label_2.setStyleSheet("background-color:rgb(15, 86, 90)")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Login_Window)
        self.username.setGeometry(QtCore.QRect(60, 50, 191, 31))
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Login_Window)
        self.password.setGeometry(QtCore.QRect(60, 150, 191, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.Login = QtWidgets.QPushButton(Login_Window)
        self.Login.setGeometry(QtCore.QRect(80, 250, 161, 61))
        self.Login.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"font-size: 30px;\n"
"color: white")
        self.Login.setObjectName("Login")
        self.registration = QtWidgets.QPushButton(Login_Window)
        self.registration.setGeometry(QtCore.QRect(90, 330, 141, 41))
        self.registration.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"font-size: 25px;\n"
"color: white")
        self.registration.setObjectName("registration")
        self.registration.clicked.connect(self.registration_window)

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def registration_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.window)
        self.window.show()



    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "LogIn"))
        self.label.setText(_translate("Login_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_2.setText(_translate("Login_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.registration.setText(_translate("Login_Window", "Registration"))
        self.Login.setText(_translate("Login_Window", "LogIn"))

















class Window(QtWidgets.QMainWindow, Ui_Login_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())