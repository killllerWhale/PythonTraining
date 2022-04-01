import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from calculator import Ui_calculator


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_calculator()
        self.ui.setupUi(self)
        self.start()
        self.checkin_completion = 0

    def start(self):
        #кнопки цифр
        self.ui.pushButton_0.clicked.connect(lambda:self.setLable("0"))
        self.ui.pushButton_1.clicked.connect(lambda:self.setLable("1"))
        self.ui.pushButton_2.clicked.connect(lambda:self.setLable("2"))
        self.ui.pushButton_3.clicked.connect(lambda:self.setLable("3"))
        self.ui.pushButton_4.clicked.connect(lambda:self.setLable("4"))
        self.ui.pushButton_5.clicked.connect(lambda:self.setLable("5"))
        self.ui.pushButton_6.clicked.connect(lambda:self.setLable("6"))
        self.ui.pushButton_7.clicked.connect(lambda:self.setLable("7"))
        self.ui.pushButton_8.clicked.connect(lambda:self.setLable("8"))
        self.ui.pushButton_9.clicked.connect(lambda:self.setLable("9"))
        # кнопки действий
        self.ui.pushButton_delete.clicked.connect(lambda:self.delete())
        self.ui.pushButton_minus.clicked.connect(lambda: self.setAction("-"))
        self.ui.pushButton_multiplication.clicked.connect(lambda: self.setAction("*"))
        self.ui.pushButton_share.clicked.connect(lambda: self.setAction("/"))
        self.ui.pushButton_plus.clicked.connect(lambda: self.setAction("+"))
        self.ui.pushButton_point.clicked.connect(lambda: self.setLable("."))
        self.ui.pushButton_result.clicked.connect(lambda: self.result())

    def setLable(self, namber):
        if self.checkin_completion == 1:
            self.checkin_completion = 0
            one = namber
        else:
            one = self.ui.label_3.text()
            one += namber
        self.ui.label_3.setText(one)

    def setAction(self, action):
        if action == "+":
            if not(not self.ui.label_3.text()):
                self.ui.label_2.setText(self.ui.label_3.text())
            self.ui.label_3.setText("")
            self.ui.label.setText("+")
        if action == "-":
            if  not(not self.ui.label_3.text()):
                self.ui.label_2.setText(self.ui.label_3.text())
            self.ui.label_3.setText("")
            self.ui.label.setText("-")
        if action == "*":
            if  not(not self.ui.label_3.text()):
                self.ui.label_2.setText(self.ui.label_3.text())
            self.ui.label_3.setText("")
            self.ui.label.setText("*")
        if action == "/":
            if  not(not self.ui.label_3.text()):
                self.ui.label_2.setText(self.ui.label_3.text())
            self.ui.label_3.setText("")
            self.ui.label.setText("/")

    def result(self):
        try:
            result = eval(self.ui.label_2.text()+self.ui.label.text()+self.ui.label_3.text())
            self.ui.label.setText("")
            self.ui.label_2.setText("")
            self.ui.label_3.setText("Результат: " + str(result))
            self.checkin_completion += 1
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Такие действия противоречать логике математики! ")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            self.ui.label.setText("")
            self.ui.label_2.setText("")
            self.ui.label_3.setText("")

    def delete(self):
        #Remove_last = Str[:-1]
        if not self.ui.label_3.text():
            if not self.ui.label.text():
                if not self.ui.label_2.text():
                    pass
                else:
                    self.ui.label_2.setText(self.ui.label_2.text()[:-1])
            else:
                self.ui.label.setText(self.ui.label.text()[:-1])
        else:
            self.ui.label_3.setText(self.ui.label_3.text()[:-1])

if __name__ == '__main__':
    app = QApplication([])
    application = Calculator()
    application.show()
    sys.exit(app.exec())