from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic


class IronMan(QMainWindow):
    def __init__(self):
        super(IronMan, self).__init__()
        uic.loadUi("pay.ui", self)

        self.cash = []

        self.q_label = self.findChild(QLabel, "q_label")
        self.d_label = self.findChild(QLabel, "d_label")
        self.n_label = self.findChild(QLabel, "n_label")
        self.p_label = self.findChild(QLabel, "p_label")
        self.q_line = self.findChild(QLineEdit, "q_line")
        self.d_line = self.findChild(QLineEdit, "d_line")
        self.n_line = self.findChild(QLineEdit, "n_line")
        self.p_line = self.findChild(QLineEdit, "p_line")
        self.pay_button = self.findChild(QPushButton, "pay_button")

        self.only_int = QIntValidator()
        self.q_line.setValidator(self.only_int)
        self.d_line.setValidator(self.only_int)
        self.n_line.setValidator(self.only_int)
        self.p_line.setValidator(self.only_int)

        self.pay_button.clicked.connect(self.enter_money)

        self.show()

    def enter_money(self):
        quarter = self.q_line.text()
        dime = self.d_line.text()
        nickle = self.n_line.text()
        penny = self.p_line.text()
        with open("chincho.txt", "w") as file:
            file.write(f"{quarter, dime, nickle, penny}")
            file.close()
            pass
        self.close()
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    iron = IronMan()
    sys.exit(app.exec_())