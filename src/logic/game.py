from random import randint
try:
    from logic.square import Square
except ImportError:
    from square import Square


class Game:
    """pelin logiikasta vastaava luokka
    """

    def __init__(self, bombs=7, size=15):
        """konstruktori, luo uuden pelin

        Args:
            bombs (int, optional): [description]. Defaults to 7.
            size (int, optional): [description]. Defaults to 15.
        """
        self.bombs = bombs
        self.board = []
        self.size = size
        self._create_board()
        self._add_bombs()
        self.bombs_without_flag = bombs

    def _create_board(self):
        """
        luo pelilaudan
        """
        for __ in range(0, self.size):
            row = []
            for _ in range(0, self.size):
                block = Square()
                row.append(block)
            self.board.append(row)

    def _add_bombs(self):
        """lisää pelilautaan pommit randintin avulla
        """
        bombs_left = self.bombs
        while bombs_left > 0:
            x_coord = randint(0, self.size - 1)
            y_coord = randint(0, self.size - 1)
            block = self.board[y_coord][x_coord]
            if not block.bomb:
                bombs_left -= 1
                block.bomb = True

    def _count_bombs_around_block(self, x_coord, y_coord):
        """käy läpi ympäröivät ruudt ja laskee niistä löytyvät pommit

        Args:
            x_coord ([int]): x-koordinaatti
            y_coord ([int]): y-koordinaatti

        Returns:
            bomb_count: ympäröivien pommien lukumäärä
        """
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
        """ käsittelee leftclikin

        Args:
            x_coord ([int]): x-koordinaatti
            y_coord ([int]): y-koordinaatti

        Returns:
            Bool: True, jos peliä ei hävitty, False, jos klikattu ruutu on pommi -> peli on hävitty
        """
        block = self.board[y_coord][x_coord]
        if block.flag:
            return True
        if block.bomb:
            return False
        self._open_block(x_coord, y_coord)
        return True

    def _open_block(self, x_coord, y_coord):
        """ avaa ruudun, jos ruudun ympärillä on 0 pommia kutsuu funktion _open_neighbours

        Args:
            x_coord ([int]): x-koordinaatti
            y_coord ([int]): y-koordinaatti
        """
        block = self.board[y_coord][x_coord]
        if not block.open:
            self._count_bombs_around_block(x_coord, y_coord)
            block.open = True
            if block.bombs_around == 0:
                self._open_neighbours(x_coord, y_coord)

    def _open_neighbours(self, x_coord, y_coord):
        """käy läpi ruudun naapurit ja avaa ne

        Args:
            x_coord ([int]): x-koordinaatti
            y_coord ([int]): y-koordinaatti
        """
        for i in range(y_coord-1, y_coord+2):
            for j in range(x_coord-1, x_coord+2):
                if i == y_coord and j == x_coord:
                    continue
                if i > -1 and i < self.size and j > -1 and j < self.size:
                    if not self.board[i][j].open:
                        self._open_block(j, i)

    def handle_rightclick_on_board(self, x_coord, y_coord):
        """käsittelee rightclikkauksen

        Args:
            x_coord ([int]): x-koordinaatti
            y_coord ([int]): y-koordinaatti
        """
        self.board[y_coord][x_coord].flagging()
        block = self.board[y_coord][x_coord]
        if block.bomb:
            if block.flag:
                self.bombs_without_flag -= 1
            elif not block.flag:
                self.bombs_without_flag += 1
