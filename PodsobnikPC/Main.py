import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
import re
from Regidtr import Ui_MainWindow2
from Vchod import Ui_MainWindow
import test

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1 = Ui_MainWindow2()
        self.ui1.setupUi(self)
        self.start()

    def start(self):
        self.ui1.pushButtonGo.clicked.connect(lambda: self.login())
        self.ui1.pushButtonVchod.clicked.connect(lambda: self.goLogin())

    def login(self):
        regexEmail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        name = self.ui1.lineEdit.text()
        email = self.ui1.lineEdit_2.text()
        password = self.ui1.lineEdit_3.text()
        passwordRepit = self.ui1.lineEdit_4.text()
        if re.match(r"^[а-яА-Я0-9]+$", name):
            if re.fullmatch(regexEmail, email):
                if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
                    if password == passwordRepit:
                        count = 0
                        file = open("test.txt", "r+")
                        for line in file:
                            line = line.split(";")
                            if line[0] == email:
                                self.erorr("Этот email уже зарегистрирован! ")
                                count = 1
                                break
                        if count == 0:
                            result = email+";"+name+";"+password+";"
                            file.write("\n"+result)
                        file.close()
                    else:
                        self.erorr("Пароли не совподают! ")
                else:
                    self.erorr("Пароль должен содержать не менее 8 символов "
                               "\nДолжен быть ограничен, хотя специально не требует ни одного из:"
                               "\nзаглавные буквы: A-Z "
                               "\nстрочные буквы: a-z"
                               "\nчисла: 0-9"
                               "\nлюбой из специальных символов: @#$%^&+=)")
            else:
                self.erorr("Неверный формат емаил!")
        else:
            self.erorr("Имя пользователя может содержать буквы (а–я), цифры (0–9)."
                       "\nЗапрещено использовать амперсанд (&), собаку(@), знаки равенства (=) и сложения (+)"
                       "\nскобки (<>), запятую (,), символ подчеркивания (_), апостроф ('), дефис (-) и точки.")

    def erorr(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def goLogin(self):
        self.chatWindow = Podsobnic()
        self.chatWindow.show()
        self.hide()

class Podsobnic(QMainWindow):
    def __init__(self):
        super(Podsobnic, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start()

    def start(self):
        self.chatWindow = ChatWindow()
        self.ui.pushButtonGo.clicked.connect(lambda: self.login())
        self.ui.pushButtonRegistr.clicked.connect(lambda: self.registr())

    def login(self):
        passw = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit.text()

        count = 0
        file = open("test.txt", "r+")
        for line in file:
            line = line.split(";")
            if line[0] == email:
                if line[2] == passw:
                    count = 0
                    self.erorr("Вы вошли", "Успех!")
                    break
                else:
                    count = 1
            else:
                count = 1
        if count == 1:
            self.erorr("Неверный логин или пароль!","Ошибка")
        file.close()


    def registr(self):
        self.chatWindow.show()
        self.hide()

    def erorr(self, text, status):
        msg = QMessageBox()
        msg.setWindowTitle(status)
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Podsobnic()
    application.show()
    sys.exit(app.exec())

