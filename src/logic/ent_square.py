class Square:
    def __init__(self) -> None:
        self.bomb = False
        self.open = False
        self.flag = False
        self.bombs_around = None
    
    def flagging(self):
        if self.flag == False:
            self.flag = True
        else:
            self.flag = False
    
    def opening(self):
        #self.bombs =count_bombs_around()
        pass

if __name__ == "__main__":
    c = Square()
    print(c.flag)
    c.flagging()
    print(c.flag)
