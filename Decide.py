from Available_menu import Espresso, Latte, Cappuccino

class Decision:
    def __init__(self, quarter, dime, nickle, penny):
        self.quarter = quarter
        self.dime = dime
        self.nickle = nickle
        self.penny = penny
    
    def count_money(self):
        self.total = (self.quarter * 0.25) + (self.dime * 0.1) + (self.nickle * 0.05) + (self.penny * 0.01)
        return self.total

    def check_enough_money(self, coffee_type, entered_money):
        esp = Espresso()
        lat = Latte()
        cap = Cappuccino()
        if coffee_type == "espresso":
            if entered_money >= esp.cost:
                return True
        elif coffee_type == "latte":
            if entered_money >= lat.cost:
                return True
        elif coffee_type == "cappuccino":
            if entered_money >= cap.cost:
                return True
    
    def check_enough_stock(self, coffee_type, water, milk, coffee):
        esp = Espresso()
        lat = Latte()
        cap = Cappuccino()
        if coffee_type == "espresso":
            if water >= esp.water:
                if coffee >= esp.coffee:
                    return True
        elif coffee_type == "latte":
            if water >= lat.water:
                if milk >= lat.milk:
                    if coffee >= lat.coffee:
                        return True
        elif coffee_type == "cappuccino":
            if water >= cap.water:
                if milk >= cap.milk:
                    if coffee >= cap.coffee:
                        return True
    