from random import randint
# import apparently works differently from commandline and vsc
try:
    from logic.square import Square
except ImportError:
    from square import Square


class Game:
    def __init__(self, bombs=70, size=15):
        self.bombs = bombs
        self.board = []
        self.size = size
        self._create_board()
        self._add_bombs()

    def _create_board(self):
        for __ in range(0, self.size):
            row = []
            for _ in range(0, self.size):
                block = Square()
                row.append(block)
            self.board.append(row)

    def _add_bombs(self):
        bombs_left = self.bombs
        while bombs_left > 0:
            x_coord = randint(0, self.size - 1)
            y_coord = randint(0, self.size - 1)
            block = self.board[y_coord][x_coord]
            if not block.bomb:
                bombs_left -= 1
                block.bomb = True

    def _count_bombs_around_block(self, x_coord, y_coord):
        bomb_count = 0
        for i in range(y_coord-1, y_coord+2):
            for j in range(x_coord-1, x_coord+2):
                if i == y_coord and j == x_coord:
                    continue
                if i > -1 and i < self.size and j > -1 and j < self.size:
                    if self.board[i][j].bomb:
                        bomb_count += 1
        self.board[y_coord][x_coord].bombs_around = bomb_count
        return bomb_count

    def handle_leftclick_on_board(self, x_coord, y_coord):
        block = self.board[y_coord][x_coord]
        if block.bomb:
            return False
            # game over
        self._open_block(x_coord, y_coord)
        return True

    def _open_block(self, x_coord, y_coord):
        block = self.board[y_coord][x_coord]
        if block.open == False:
            self._count_bombs_around_block(x_coord, y_coord)
            block.open = True
            if block.bombs_around == 0:
                # self._open_neighbours(x_coord, y_coord) #this creates recursionerror :)))
                # print(bomb_count)
                pass
            

    def _open_neighbours(self, x_coord, y_coord):
        for i in range(y_coord-1, y_coord+2):
            for j in range(x_coord-1, x_coord+2):
                if i == y_coord and j == x_coord:
                    continue
                if i > -1 and i < self.size and j > -1 and j < self.size:
                    if self.board[i][j].open == False:
                        self._open_block(j, i)

    def handle_rightclick_on_board(self, x_coord, y_coord):
        self.board[y_coord][x_coord].flagging()
