class Command:
    def __init__(self):
        self.hello = "hello, world"
    
    def enable_buttons(self, first, second, third, fourth, fifth, sixth):
        first.setEnabled(True)
        second.setEnabled(True)
        third.setEnabled(True)
        fourth.setEnabled(True)
        fifth.setEnabled(True)
        sixth.setEnabled(True)
    
    def disable_buttons(self, first, second, third, fourth, fifth, sixth):
        first.setEnabled(False)
        second.setEnabled(False)
        third.setEnabled(False)
        fourth.setEnabled(False)
        fifth.setEnabled(False)
        sixth.setEnabled(False)

