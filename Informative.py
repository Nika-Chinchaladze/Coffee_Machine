from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from Available_menu import Espresso, Latte, Cappuccino
import pandas as pd


class LoadInfo(QMainWindow):
    def __init__(self):
        super(LoadInfo, self).__init__()
        uic.loadUi("info.ui", self)
        # variables:
        self.esp = Espresso()
        self.lat = Latte()
        self.cap = Cappuccino()
        self.stock = pd.DataFrame({"Water - ml":[self.esp.water, self.lat.water, self.cap.water],
                                   "Milk - ml":[self.esp.milk, self.lat.milk, self.cap.milk],
                                   "Coffee - g":[self.esp.coffee, self.lat.coffee, self.cap.coffee],
                                   "Cost - $":[self.esp.cost, self.lat.cost, self.cap.cost]},
                                   index=["Espresso", "Latte", "Cappuccino"])
        # content:
        self.close_button = self.findChild(QPushButton, "close_button")
        self.table_widget = self.findChild(QTableWidget, "table_widget")
        # execution:
        self.close_button.clicked.connect(lambda: self.close())
        self.show()
    
    def display_data(self):
        row_number = len(self.stock.index)
        col_number = len(self.stock.columns)

        self.table_widget.setColumnCount(col_number)
        self.table_widget.setRowCount(row_number)
        self.table_widget.setHorizontalHeaderLabels(self.stock.columns)
        self.table_widget.setVerticalHeaderLabels(self.stock.index)

        for rows in range(row_number):
            for columns in range(col_number):
                self.table_widget.setItem(rows, columns, QTableWidgetItem(str(self.stock.iat[rows, columns])))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    adin = LoadInfo()
    sys.exit(app.exec_())