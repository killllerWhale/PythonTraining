import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.run)

        self.show()

    def run(self):
        i, okBtnPressed = QInputDialog.getText(self, "Введите имя",
                                               "Как тебя зовут?")
        if okBtnPressed:
            self.button_1.setText(i)

        i, okBtnPressed = QInputDialog.getInt(self, "Введите возраст",
                                              "Сколько тебе лет?", 19, 18, 25, 1)
        if okBtnPressed:
            self.button_1.setText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())