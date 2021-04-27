import pygame
try:
    from logic.game import Game
except ImportError:
    from game import Game


class Ui:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 24)
        self.font2 = pygame.font.SysFont("Arial", 20)
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Minesweeper BETA")
        self.view = "menu"
        self.game = None
        self.block_size = 20
        self._run()

    def _run(self):
        while True:
            self._draw_view()
            self._handle_events()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if self.view == "menu":
                self._handle_events_in_menu(event)
            elif self.view == "game":
                self._handle_events_in_game(event)

    def _handle_events_in_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 273 and event.pos[0] < 383 and event.pos[1] > 106 and event.pos[1] < 122:
                    # painoit nappia 1 kohdassa (273, 106) painoit nappia 1 kohdassa(383, 122)
                    #print("painoit nappia", event.button, "kohdassa", event.pos)
                    self.view = "game"
                    self.game = Game()

    def _handle_events_in_game(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # painoit nappia 1 kohdassa (56, 33)
                if event.pos[0] > 5 and event.pos[0] < 55 and event.pos[1] > 10 and event.pos[1] < 33:
                    self.view = "menu"
                    #print("painoit nappia", event.button, "kohdassa", event.pos)
                elif event.pos[0] > 20+ self.block_size and event.pos[0] < 300 and event.pos[1] > 60 + self.block_size and event.pos[1] < 360:
                    #grid!
                    x = event.pos[0] - 20 - self.block_size
                    y = event.pos[1] - 60 - self.block_size
                    x = x // 20
                    y = y // 20
                    if not self.game.handle_leftclick_on_board(x, y):
                        pass
                        #game over
            elif event.button == 3:
                if event.pos[0] > 20 + self.block_size and event.pos[0] < 300 and event.pos[1] > 60 + self.block_size and event.pos[1] < 360:
                    #grid!
                    x = event.pos[0] - 20 - self.block_size
                    y = event.pos[1] - 60 - self.block_size
                    x = x // 20
                    y = y // 20
                    self.game.handle_rightclick_on_board(x,y)

                #print("painoit nappia", event.button, "kohdassa", event.pos)

    def _draw_view(self):
        self.screen.fill((255, 255, 255))
        if self.view == "menu":
            self._draw_menu()
        elif self.view == "game":
            self._draw_game()
        pygame.display.flip()

    def _draw_game(self):
        self._draw_grid()
        self._draw_board()
        text_minesweeper = self.font.render("Minesweeper", True, (0, 0, 0))
        self.screen.blit(text_minesweeper, (280, 10))
        text_back = self.font.render("Back", True, (0, 0, 0))
        self.screen.blit(text_back, (5, 10))

    def _draw_grid(self):
        for x in range(20 + self.block_size, 300, self.block_size):
            for y in range(60 + self.block_size, 60 + 300, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (127, 127, 127), rect, 1)

    def _draw_board(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.board[i][j].flag:
                    #draw flag
                    flag = self.font2.render("F", True, (0,0,0))
                    self.screen.blit(flag, (20+ self.block_size + (j * self.block_size), 60 + self.block_size + (i* self.block_size)))
                elif self.game.board[i][j].open:
                    num = self.font2.render(str(self.game.board[i][j].bombs_around), True, (0, 0, 0))
                    self.screen.blit(num, (20 + self.block_size + (j * self.block_size),60 + self.block_size + (i * self.block_size)))
                    

    def _draw_menu(self):
        text_new_game = self.font.render("New game", True, (0, 0, 0))
        self.screen.blit(text_new_game, (270, 100))
