import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 592)
        MainWindow.setMinimumSize(QtCore.QSize(386, 592))
        MainWindow.setMaximumSize(QtCore.QSize(386, 592))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 381, 191))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(270, 190, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 190, 271, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("       Введите текст для заметки...")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 210, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 240, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 240, 321, 31))
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 321, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 321, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 360, 321, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 321, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 321, 31))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 480, 321, 31))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 520, 321, 31))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 280, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 320, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 360, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 400, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 440, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 480, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 520, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(220, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "add"))
        self.pushButton_2.setText(_translate("MainWindow", "delete"))
        self.pushButton_3.setText(_translate("MainWindow", "delete"))
        self.pushButton_4.setText(_translate("MainWindow", "delete"))
        self.pushButton_5.setText(_translate("MainWindow", "delete"))
        self.pushButton_6.setText(_translate("MainWindow", "delete"))
        self.pushButton_7.setText(_translate("MainWindow", "delete"))
        self.pushButton_8.setText(_translate("MainWindow", "delete"))
        self.pushButton_9.setText(_translate("MainWindow", "delete"))


class Daily_planner(QMainWindow):
    def __init__(self):
        super(Daily_planner, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes_dates = {}
        self.start()

    def start(self):
        self.ui.calendarWidget.clicked.connect(lambda :self.dispdate())
        self.ui.pushButton.clicked.connect(lambda: self.setText())
        self.ui.pushButton_2.clicked.connect(lambda: self.deleteText(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.deleteText(2))
        self.ui.pushButton_4.clicked.connect(lambda: self.deleteText(3))
        self.ui.pushButton_5.clicked.connect(lambda: self.deleteText(4))
        self.ui.pushButton_6.clicked.connect(lambda: self.deleteText(5))
        self.ui.pushButton_7.clicked.connect(lambda: self.deleteText(6))
        self.ui.pushButton_8.clicked.connect(lambda: self.deleteText(7))
        self.ui.pushButton_9.clicked.connect(lambda: self.deleteText(8))

    def deleteText(self,number):
        if self.ui.dateEdit.date() in self.notes_dates:
            if self.notes_dates[self.ui.dateEdit.date()] == []:
                self.setWrong("На эту дату заметок нет")
                return
            texts = self.notes_dates[self.ui.dateEdit.date()]
            texts.pop(number-1)
            self.notes_dates[self.ui.dateEdit.date()] = texts
            self.dispdate()
        else:
            self.setWrong("На эту дату заметок нет")

    def dispdate(self):
        self.ui.label_1.setText("")
        self.ui.label_2.setText("")
        self.ui.label_3.setText("")
        self.ui.label_4.setText("")
        self.ui.label_5.setText("")
        self.ui.label_6.setText("")
        self.ui.label_7.setText("")
        self.ui.label_8.setText("")
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
        if self.ui.dateEdit.date() in self.notes_dates:
            if len(self.notes_dates[self.ui.dateEdit.date()])==1:
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==2:
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==3:
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
                self.ui.label_3.setText(self.notes_dates[self.ui.dateEdit.date()][2])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==4:
                self.ui.label_4.setText(self.notes_dates[self.ui.dateEdit.date()][3])
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
                self.ui.label_3.setText(self.notes_dates[self.ui.dateEdit.date()][2])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==5:
                self.ui.label_5.setText(self.notes_dates[self.ui.dateEdit.date()][4])
                self.ui.label_4.setText(self.notes_dates[self.ui.dateEdit.date()][3])
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
                self.ui.label_3.setText(self.notes_dates[self.ui.dateEdit.date()][2])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==6:
                self.ui.label_6.setText(self.notes_dates[self.ui.dateEdit.date()][5])
                self.ui.label_5.setText(self.notes_dates[self.ui.dateEdit.date()][4])
                self.ui.label_4.setText(self.notes_dates[self.ui.dateEdit.date()][3])
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
                self.ui.label_3.setText(self.notes_dates[self.ui.dateEdit.date()][2])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==7:
                self.ui.label_7.setText(self.notes_dates[self.ui.dateEdit.date()][6])
                self.ui.label_6.setText(self.notes_dates[self.ui.dateEdit.date()][5])
                self.ui.label_5.setText(self.notes_dates[self.ui.dateEdit.date()][4])
                self.ui.label_4.setText(self.notes_dates[self.ui.dateEdit.date()][3])
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
                self.ui.label_3.setText(self.notes_dates[self.ui.dateEdit.date()][2])
            elif len(self.notes_dates[self.ui.dateEdit.date()])==8:
                self.ui.label_8.setText(self.notes_dates[self.ui.dateEdit.date()][7])
                self.ui.label_7.setText(self.notes_dates[self.ui.dateEdit.date()][6])
                self.ui.label_6.setText(self.notes_dates[self.ui.dateEdit.date()][5])
                self.ui.label_5.setText(self.notes_dates[self.ui.dateEdit.date()][4])
                self.ui.label_4.setText(self.notes_dates[self.ui.dateEdit.date()][3])
                self.ui.label_2.setText(self.notes_dates[self.ui.dateEdit.date()][1])
                self.ui.label_1.setText(self.notes_dates[self.ui.dateEdit.date()][0])
                self.ui.label_3.setText(self.notes_dates[self.ui.dateEdit.date()][2])

    def setText(self):
        if self.ui.textEdit.toPlainText()=="":
            self.setWrong("Нельзя добавить пустое поле!")
            self.ui.textEdit.setText("")
            return
        if self.ui.dateEdit.date() in self.notes_dates:
            if len(self.notes_dates[self.ui.dateEdit.date()]) < 8:
                texts = self.notes_dates[self.ui.dateEdit.date()]
                texts.append(self.ui.textEdit.toPlainText())
                self.notes_dates[self.ui.dateEdit.date()] = texts
            else:
                self.setWrong("На данный момент все ячейки заняты!")
        else:
            texts = [self.ui.textEdit.toPlainText()]
            self.notes_dates[self.ui.dateEdit.date()] = texts
        self.ui.textEdit.setText("")
        self.dispdate()

    def setWrong(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка!")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication([])
    application = Daily_planner()
    application.show()
    sys.exit(app.exec())