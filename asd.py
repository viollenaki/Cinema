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
        self.label = QtWidgets.QLabel(Registration)
        self.label.setGeometry(QtCore.QRect(40, 10, 231, 31))
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"border-radius: 15px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Registration)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 231, 31))
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"border-radius: 15px")
        self.label_2.setObjectName("label_2")
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
        self.label_3 = QtWidgets.QLabel(Registration)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 231, 31))
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"border-radius: 15px")
        self.label_3.setObjectName("label_3")
        self.sign_up = QtWidgets.QPushButton(Registration)
        self.sign_up.setGeometry(QtCore.QRect(40, 280, 231, 71))
        self.sign_up.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 30px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius:30px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 30px\n"
"}\n"
"")
        self.sign_up.setObjectName("sign_up")

        self.sign_up.clicked.connect(self.sign_up_clicked)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration"))
        self.label.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_2.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.label_3.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Confirm Password</span></p></body></html>"))
        self.sign_up.setText(_translate("Registration", "Sign Up"))



    def sign_up_clicked(self):
        username = self.username.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if password == confirm_password:
            # Используем 'params' для GET-запроса
            response = requests.get('http://viollenaki.pythonanywhere.com/get_user', params={'username': username})
            
            if response.json() == False:  # Если пользователь не найден
                # Используем 'params' для добавления пользователя
                requests.get('http://viollenaki.pythonanywhere.com/add_user', params={'username': username, 'password': password})
                
                QtWidgets.QMessageBox.information(self, "Success", "Registration successful.")
                self.close()  # Закрываем окно регистрации
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Username already exists.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Passwords do not match.")




class Ui_Login_Window(QtWidgets.QWidget):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(300, 400)
        Login_Window.setMaximumSize(QtCore.QSize(300, 400))
        Login_Window.setStyleSheet("background-color:rgb(148, 143, 124)")
        self.label = QtWidgets.QLabel(Login_Window)
        self.label.setGeometry(QtCore.QRect(60, 10, 191, 31))
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 10px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login_Window)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 191, 31))
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 10px")
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
        self.login_button = QtWidgets.QPushButton(Login_Window)
        self.login_button.setGeometry(QtCore.QRect(80, 250, 161, 61))
        self.login_button.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 30px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 30px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 30px\n"
"}\n"
"")
        self.login_button.setObjectName("login_button")

        self.login_button.clicked.connect(self.login_clicked)

        self.registration_button = QtWidgets.QPushButton(Login_Window)
        self.registration_button.setGeometry(QtCore.QRect(90, 330, 141, 41))
        self.registration_button.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.registration_button.setObjectName("registration_button")

        self.registration_button.clicked.connect(self.registration_window)

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Dialog"))
        self.label.setText(_translate("Login_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Username</span></p></body></html>"))
        self.label_2.setText(_translate("Login_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.login_button.setText(_translate("Login_Window", "LogIn"))
        self.registration_button.setText(_translate("Login_Window", "Registration"))




    def registration_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.window)
        self.window.show()

    def login_clicked(self):
        global user_now
        username = self.username.text()
        password = self.password.text()
        url = 'http://viollenaki.pythonanywhere.com/get_user'
        response = requests.get(url, params={'username': username})
        if response.json() == True:
            url = 'http://viollenaki.pythonanywhere.com/check_password'
            response = requests.get(url, params={'username': username, 'password': password})
            if response.json() == True:
                user_now = username
                self.close()

                # Создаем главное окно
                self.window = QtWidgets.QWidget()
                self.ui = Ui_Main_wind()
                self.ui.setupUi(self.window)

                # Получаем разрешение экрана
                screen = QtWidgets.QApplication.primaryScreen()
                screen_rect = screen.availableGeometry()

                # Размер окна
                window_size = self.window.geometry()
                window_width = window_size.width()
                window_height = window_size.height()

                # Рассчитываем координаты для центрирования окна
                x = (screen_rect.width() - window_width) // 2
                y = (screen_rect.height() - window_height) // 2

                # Перемещаем окно в центр экрана
                self.window.move(x, y)

                # Показываем окно
                self.window.show()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Incorrect password.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "User not found.")




class Ui_Main_wind(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 550)
        Form.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.movie_now = None
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 251, 41))
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px")
        self.label_2.setObjectName("label_2")
        self.history = QtWidgets.QPushButton(Form)
        self.history.setGeometry(QtCore.QRect(449, 470, 141, 51))
        self.history.setStyleSheet("QPushButton:hover{\n"
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
        self.history.setObjectName("history")
        self.info = QtWidgets.QPushButton(Form)
        self.info.setGeometry(QtCore.QRect(60, 470, 130, 51))
        self.info.setStyleSheet("QPushButton:hover{\n"
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
        self.info.setObjectName("info")
        self.buy_tickets = QtWidgets.QPushButton(Form)
        self.buy_tickets.setGeometry(QtCore.QRect(260, 470, 130, 51))
        self.buy_tickets.setStyleSheet("QPushButton:hover{\n"
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
        self.buy_tickets.setObjectName("buy_tickets")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 251, 41))
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px")
        self.label.setObjectName("label")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(0, 660, 121, 41))
        self.exit_button.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 20px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.movies_list = QtWidgets.QListWidget(Form)
        self.movies_list.setGeometry(QtCore.QRect(40, 80, 260, 370))
        self.movies_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.movies_list.setObjectName("movies_list")
        self.movies_list.itemDoubleClicked.connect(self.fill_seance_table)   

        self.seance_list = QtWidgets.QListWidget(Form)
        self.seance_list.setGeometry(QtCore.QRect(340, 80, 260, 370))
        self.seance_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.seance_list.setObjectName("seance_list")
        # self.seance_list.itemDoubleClicked.connect(self.buy_ticket)

        self.retranslateUi(Form)
        self.fill_film_table()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Seance</p></body></html>"))
        self.history.setText(_translate("Form", "HISTORY"))
        self.info.setText(_translate("Form", "INFO"))
        self.buy_tickets.setText(_translate("Form", "BUY"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Movies</p></body></html>"))
        self.exit_button.setText(_translate("Form", "EXIT"))

    def fill_film_table(self):
        response = requests.get('http://viollenaki.pythonanywhere.com/get_films').json()
        films = [i for i in response.keys()]
        for i in films:
            self.movies_list.addItem(i)




    def fill_seance_table(self):
        self.seance_list.clear()
        selected_movie = self.movies_list.selectedItems()[0].text()
        response = requests.get('http://viollenaki.pythonanywhere.com/get_seances', params={'film': selected_movie}).json()
        seances = [i for i in response.keys()]
        for i in seances:
            self.seance_list.addItem(i)














class Window(QtWidgets.QMainWindow, Ui_Login_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())