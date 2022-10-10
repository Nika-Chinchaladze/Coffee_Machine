from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtWidgets
from PyQt5 import uic
from ReadTxt import Writting


class SecretPass(QMainWindow):
    def __init__(self):
        super(SecretPass, self).__init__()
        uic.loadUi("pass.ui", self)

        # content:
        self.check_button = self.findChild(QPushButton, "check_button")
        self.money_label = self.findChild(QLabel, "money_label")
        self.pass_line = self.findChild(QLineEdit, "pass_line")
        self.pass_line.setPlaceholderText("password")
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)

        self.check_button.clicked.connect(self.grab_money)
        self.show()
    
    def grab_money(self):
        txt = Writting()
        txt_chash = txt.read_from_text()
        if self.pass_line.text() == "chincho":
            self.money_label.setText(f"{txt_chash} $")
            self.money_label.setStyleSheet("background-color: rgb(152, 255, 159);")
        else:
            self.money_label.setText("Wrong Password, Are You Owner?")
            self.money_label.setStyleSheet("background-color: rgb(255, 184, 170);")
        self.pass_line.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    secr = SecretPass()
    sys.exit(app.exec_())