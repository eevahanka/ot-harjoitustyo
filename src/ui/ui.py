import pygame

from logic.game import Game

class Ui:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 24)
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Minesweeper BETA")
        self.view = "menu"
        self._run()

    def _run(self):
        while True:
            self._draw_view()
            self._handle_events()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k and self.view == "menu":
                    self.view = "game"
                    game = Game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #painoit nappia 1 kohdassa (56, 33)
                    if event.pos[0] > 5 and event.pos[0] < 55 and event.pos[1] > 10 and event.pos[1] < 33:
                        self.view = "menu"
                    #print("painoit nappia", event.button, "kohdassa", event.pos)

    def _draw_view(self):
        self.screen.fill((255, 255, 255))
        if self.view == "menu":
            self._draw_menu()
        if self.view == "game":
            self._draw_game()
        pygame.display.flip()

    def _draw_game(self):
        self._draw_grid()
        self._draw_board()
        text_minesweeper = self.font.render( "Minesweeper", True, (0, 0, 0))
        self.screen.blit(text_minesweeper, (280, 10))
        text_back = self.font.render("Back", True, (0, 0, 0))
        self.screen.blit(text_back, (5, 10))



    def _draw_grid(self):
        block_size = 20
        for x in range(20 +block_size, 300, block_size):
            for y in range(60 + block_size, 60 +300, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(self.screen, (127, 127, 127), rect, 1)

    def _draw_board(self):
        pass

    def _draw_menu(self):
        text_new_game = self.font.render("New game (press 'k') ", True, (0, 0, 0))
        self.screen.blit(text_new_game, (280, 100))
