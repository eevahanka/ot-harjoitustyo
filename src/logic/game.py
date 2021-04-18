from random import randint
#import apparently works differently from commandline and vsc
try:
    from logic.square import Square
except:
    from square import Square

class Game:
    def __init__(self, bombs=70, size=15):
        self.bombs = bombs
        self.board = []
        self.size = size
        self._create_board()
        self._add_bombs()

    def _create_board(self):
        for i in range(0, self.size):
            row = []
            for j in range(0, self.size):
                block = Square()
                row.append(block)
            self.board.append(row)
        

    def _add_bombs(self):
        bombs_left = self.bombs
        while bombs_left > 0:
            x = randint(0,self.size -1)
            y = randint(0, self.size - 1)
            block = self.board[y][x]
            if not block.bomb:
                bombs_left -= 1
                block.bomb = True

    def _count_bombs_around_block(self, x, y):
        bomb_count = 0
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if (not (i == y and j == x)) and i > -1 and i < self.size and j > -1 and j < self.size:
                    if self.board[i][j].bomb:
                        bomb_count += 1
        self.board[y][x].bombs_around = bomb_count
        return bomb_count

    def handle_leftclick_on_board(self, x, y):
        block = self.board[y][x]
        if block.bomb:
            return False
            #game over
        bomb_count = self._count_bombs_around_block(x, y)
        if bomb_count == 0:
            #open neighboursquares
            pass
        return True

    def handle_rightclick_on_board(self, x, y):
        self.board[y][x].flagging()

