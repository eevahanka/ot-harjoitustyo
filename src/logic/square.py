class Square:
    def __init__(self):
        self.bomb = False
        self.open = False
        self.flag = False
        self.bombs_around = None

    def flagging(self):
        if self.flag:
            self.flag = False
        else:
            self.flag = True
