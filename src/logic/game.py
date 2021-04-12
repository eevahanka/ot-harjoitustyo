from square import Square

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
    
    def _check_if_bomb(self, position):
        pass


if True: #__name__ == "__main__":
    game = Game()
    print(game.board)