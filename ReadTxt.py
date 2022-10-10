class Reading:
    def __init__(self):
        self.hello = 0

    def get_list(self):
        with open ("chincho.txt", "r") as file:
            var = file.read()
            file.close()
            pass
        var = var.replace("(", "")
        var = var.replace(")", "")
        var = var.replace("'", "")
        var = var.split(", ")
        new_list = [int(i) for i in var]
        return new_list


class Writting:
    def __init__(self):
        self.hello = "hello, world"
    
    def write_txt(self, quantity):
        with open("dollar.txt", "w") as file:
            file.write(f"{quantity}")
            file.close()
            pass
    
    def read_from_text(self):
        with open ("dollar.txt", "r") as file:
            var = file.read()
            file.close()
            pass
        return var

