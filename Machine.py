from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFrame
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5 import uic
from PayBox import IronMan
from Informative import LoadInfo
from Owner import SecretPass
from ReadTxt import Reading, Writting
from Decide import Decision
from Available_menu import Espresso, Latte, Cappuccino
from Refresh_section import Command


class SpiderMan(QMainWindow):
    def __init__(self):
        super(SpiderMan, self).__init__()
        uic.loadUi("machine.ui", self)
        #----------------------------#
        self.water = 500
        self.milk = 400
        self.coffee = 100
        self.money = 0

        # define content:
        self.head_label = self.findChild(QLabel, "head_label")
        self.info_label = self.findChild(QLabel, "info_label")
        self.cup_label = self.findChild(QLabel, "cup_label")
        self.place_label = self.findChild(QLabel, "place_label")
        self.cover_label = self.findChild(QLabel, "cover_label")
        self.refund_label = self.findChild(QLabel, "refund_label")
        self.cap_button = self.findChild(QPushButton, "cap_button")
        self.lat_button = self.findChild(QPushButton, "lat_button")
        self.esp_button = self.findChild(QPushButton, "esp_button")
        self.turn_button = self.findChild(QPushButton, "turn_button")
        self.take_button = self.findChild(QPushButton, "take_button")
        self.report_button = self.findChild(QPushButton, "report_button")
        self.info_button = self.findChild(QPushButton, "info_button")
        self.cash_button = self.findChild(QPushButton, "cash_button")
        self.frame_1 = self.findChild(QFrame, "frame_1")
        #------------------------------------------
        self.cap_button.setEnabled(False)
        self.lat_button.setEnabled(False)
        self.esp_button.setEnabled(False)
        self.take_button.setEnabled(False)
        self.report_button.setEnabled(False)
        self.info_button.setEnabled(False)

        # call defined methods:
        self.turn_button.clicked.connect(self.turn_on_off)
        self.esp_button.clicked.connect(self.ESPRESSO)
        self.lat_button.clicked.connect(self.LATTE)
        self.cap_button.clicked.connect(self.CAPPUCCINO)
        self.take_button.clicked.connect(self.take_coffee)
        self.report_button.clicked.connect(self.report_recources)
        self.info_button.clicked.connect(self.check_information)
        self.cash_button.clicked.connect(self.check_existing_money)

        self.show()

# ------------------------------------- logic ----------------------------------- #
    def Green(self):
        self.info_label.setStyleSheet("background-color: rgb(152, 255, 159);")
    
    def Red(self):
        self.info_label.setStyleSheet("background-color: rgb(255, 184, 170);")
    
    def Standard(self):
        self.info_label.setStyleSheet("background-color: rgb(222, 222, 166);")
    
    def check_information(self):
        self.window_info = QMainWindow()
        self.info = LoadInfo()
        self.info.display_data()
    
    def check_existing_money(self):
        self.window_secret = QMainWindow()
        self.secr = SecretPass()
        txt = Writting()
        txt.write_txt(self.money)

    
    def turn_on_off(self):
        self.Standard()
        rule = Command()
        if self.info_label.text() == "Coffee Machine is Turned OFF!":
            self.info_label.setText("Which Coffee Would You Like?")
            rule.enable_buttons(self.cap_button, self.lat_button, self.esp_button, self.take_button, self.report_button, self.info_button)
        else:
            self.info_label.setText("Coffee Machine is Turned OFF!")
            rule.disable_buttons(self.cap_button, self.lat_button, self.esp_button, self.take_button, self.report_button, self.info_button)
            self.water = 500
            self.milk = 400
            self.coffee = 100

    
    def Forward(self):
        self.anim = QPropertyAnimation(self.cup_label, b"pos")
        self.anim.setStartValue(QPoint(0, 340))
        self.anim.setEndValue(QPoint(230, 340))
        self.anim.setDuration(2000)
        self.anim.start()
    
    def Backward(self):
        self.anim = QPropertyAnimation(self.cup_label, b"pos")
        self.anim.setEndValue(QPoint(0, 340))
        self.anim.start()
    
    def ESPRESSO(self):
        self.chosen = "espresso"
        self.pay_money()
    
    def LATTE(self):
        self.chosen = "latte"
        self.pay_money()
    
    def CAPPUCCINO(self):
        self.chosen = "cappuccino"
        self.pay_money()
        
    def pay_money(self):
        self.window_pay = QMainWindow()
        self.iron = IronMan()
        self.info_label.setText("")
        self.refund_label.setText("")
        self.Backward()
        self.Standard()
    
    def take_coffee(self):
        cash = Reading()
        var = cash.get_list()
        will = Decision(var[0], var[1], var[2], var[3])
        self.paid_money = will.count_money()
        if will.check_enough_stock(self.chosen, self.water, self.milk, self.coffee):
            if will.check_enough_money(self.chosen, self.paid_money):
                self.recource_change()
                self.Forward()
                self.Green()
            else:
                self.info_label.setText("Money is not enough!")
                self.refund_label.setText(f"{self.paid_money} Refunded!")
                self.Red()
        else:
            self.info_label.setText("Sorry, Not enough Recources, try other Options!")
            self.refund_label.setText(f"{self.paid_money} Refunded!")
            self.Red()
    
    def recource_change(self):
        self.Green()
        esp = Espresso()
        lat = Latte()
        cap = Cappuccino()
        if self.chosen == "espresso":
            self.water -= esp.water
            self.coffee -= esp.coffee
            self.money += esp.cost
            if self.paid_money > esp.cost:
                sub_1 = round(self.paid_money - esp.cost, 2)
                self.info_label.setText(f"Enjoy with Your Espresso!")
                self.refund_label.setText(f"{sub_1} refund!")
            else:
                self.info_label.setText(f"Enjoy with Your Espresso!")
        elif self.chosen == "latte":
            self.water -= lat.water
            self.milk -= lat.milk
            self.coffee -= lat.coffee
            self.money += lat.cost
            if self.paid_money > lat.cost:
                sub_2 = round(self.paid_money - lat.cost,2)
                self.info_label.setText(f"Enjoy with Your Latte!")
                self.refund_label.setText(f"{sub_2} refund")
            else:
                self.info_label.setText(f"Enjoy with Your Latte!")
        elif self.chosen == "cappuccino":
            self.water -= cap.water
            self.milk -= cap.milk
            self.coffee -= cap.coffee
            self.money += cap.cost
            if self.paid_money > cap.cost:
                sub_3 = round(self.paid_money - cap.cost, 2)
                self.info_label.setText(f"Enjoy with Your Cappuccino!")
                self.refund_label.setText(f"{sub_3} refund")
            else:
                self.info_label.setText(f"Enjoy with Your Cappuccino!")

    def report_recources(self):
        self.Standard()
        self.info_label.setText(f"Water : {self.water} ml,     Milk : {self.milk} ml,     Coffee : {self.coffee} g")
        self.refund_label.setText("")

# -------------------------------------- end ------------------------------------ #

if __name__ == "__main__":
    import  sys
    app = QApplication(sys.argv)
    spider = SpiderMan()
    sys.exit(app.exec_())