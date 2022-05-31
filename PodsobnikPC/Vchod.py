# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vchod.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 596)
        MainWindow.setMinimumSize(QtCore.QSize(413, 596))
        MainWindow.setMaximumSize(QtCore.QSize(483, 596))
        MainWindow.setStyleSheet("background-color: rgb(243, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 161, 181))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Photo/Ellipse 1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, -10, 221, 111))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Photo/Ellipse 2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 510, 291, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Photo/Ellipse 3circle_entrance_three.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 430, 131, 171))
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Photo/Ellipse 4 (1).png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 170, 151, 61))
        self.label_5.setStyleSheet("font: 35pt \"Arial\";\n"
"color: rgb(68, 64, 64);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 240, 321, 41))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(252, 249, 249);\n"
"border-color: rgb(224, 218, 218);\n"
"border-radius: 20px;  ")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 280, 321, 41))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgb(252, 249, 249);\n"
"border-radius: 20px;  ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButtonGo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGo.setGeometry(QtCore.QRect(290, 250, 61, 61))
        self.pushButtonGo.setStyleSheet("border-radius: 30px;  \n"
"font: 75 25pt \"Arial\";\n"
"background-color: rgb(59, 178, 245);\n"
"color: rgb(255, 255, 255);")
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.pushButtonRegistr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRegistr.setGeometry(QtCore.QRect(20, 340, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButtonRegistr.setFont(font)
        self.pushButtonRegistr.setStyleSheet("border-radius: 20px;  \n"
"background-color: rgb(252, 249, 249);\n"
"font: 75 16pt \"Arial\";\n"
"color: rgb(68, 64, 64);")
        self.pushButtonRegistr.setObjectName("pushButtonRegistr")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.label_5.setText(_translate("MainWindow", "Вход"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "    твой номер"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "    твой пароль"))
        self.pushButtonGo.setText(_translate("MainWindow", "Go"))
        self.pushButtonRegistr.setText(_translate("MainWindow", "Регистрация"))

