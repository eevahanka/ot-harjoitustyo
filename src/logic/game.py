from logic.square import Square
#src/logic/ent_square.py

class Game:
    def __init__(self, bombs = 20):
        self.bombs = bombs
        self.board = []
        self._create_board()

    def _create_board(self, size = 15):
        for i in range(0, size):
            row = []
            for j in range(0, size):
                block = Square()
                row.append(block)
            self.board.append(row)
    
    def _add_bombs(self):
        pass

    def _check_if_bomb(self, position):
        pass


