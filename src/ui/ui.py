from datetime import datetime
import pygame
from time import sleep

try:
    from repo.game_repo import game_repo
except ImportError:
    from game_repo.py import game_repo
try:
    from logic.game import Game
except ImportError:
    from game import Game


class Ui:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 24)
        self.font2 = pygame.font.SysFont("Arial", 19)
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Minesweeper")
        self.view = "menu"
        self.game = None
        self.block_size = 20
        self.game_won = None
        self.repo = game_repo
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
            elif self.view == "stats":
                self._handle_events_in_stats(event)
            elif self.view == "game_over":
                self._handle_events_in_game_over(event)

    def _handle_events_in_menu(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 273 and event.pos[0] < 383 and event.pos[1] > 106 and event.pos[1] < 122:
                    self.view = "game"
                    self.game = Game()
                elif event.pos[0] > 270 and event.pos[0] < 325 and event.pos[1] > 155 and event.pos[1] < 173:
                    self.view = "stats"

    def _handle_events_in_game(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 5 and event.pos[0] < 55 and event.pos[1] > 10 and event.pos[1] < 33:
                    self.view = "menu"
                elif event.pos[0] > 2 * self.block_size and event.pos[0] < 300 + (2 * self.block_size) and event.pos[1] > 4 * self.block_size and event.pos[1] < (4 * self.block_size) + 300:
                    x = event.pos[0] - 20 - self.block_size
                    y = event.pos[1] - 60 - self.block_size
                    x = x // 20
                    y = y // 20
                    if not self.game.handle_leftclick_on_board(x, y):
                        self.game_won = False
                        self.view = "game_over"
            elif event.button == 3:
                if event.pos[0] > 2 * self.block_size and event.pos[0] < 300 + (2 * self.block_size) and event.pos[1] > 4 * self.block_size and event.pos[1] < (4 * self.block_size) + 300:
                    x = event.pos[0] - 20 - self.block_size
                    y = event.pos[1] - 60 - self.block_size
                    x = x // 20
                    y = y // 20
                    self.game.handle_rightclick_on_board(x, y)
        if self.game.bombs_without_flag == 0:
            self.game_won = True
            self.view = "game_over"

    def _draw_view(self):
        self.screen.fill((255, 255, 255))
        if self.view == "menu":
            self._draw_menu()
        elif self.view == "game":
            self._draw_game()
        elif self.view == "stats":
            self._draw_stats()
        elif self.view == "game_over":
            self._draw_game_over()
        pygame.display.flip()

    def _draw_game(self):
        self._draw_grid()
        self._draw_board()
        text_minesweeper = self.font.render("Minesweeper", True, (0, 0, 0))
        self.screen.blit(text_minesweeper, (280, 10))
        text_back = self.font.render("Back", True, (0, 0, 0))
        self.screen.blit(text_back, (5, 10))

    def _draw_grid(self):
        for x in range(2 * self.block_size, 300 + (2 * self.block_size), self.block_size):
            for y in range(4 * self.block_size, (4 * self.block_size) + 300, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, (127, 127, 127), rect, 1)

    def _draw_board(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.board[i][j].flag:
                    flag = self.font2.render("F", True, (0, 0, 0))
                    self.screen.blit(flag, (20 + self.block_size + (j * self.block_size),
                                     60 + self.block_size + (i * self.block_size)))
                elif self.game.board[i][j].open:
                    num = self.font2.render(
                        str(self.game.board[i][j].bombs_around), True, (0, 0, 0))
                    self.screen.blit(num, (20 + self.block_size + (j * self.block_size),
                                     60 + self.block_size + (i * self.block_size)))

    def _draw_menu(self):
        text_new_game = self.font.render("New game", True, (0, 0, 0))
        self.screen.blit(text_new_game, (270, 100))
        text_stats = self.font.render("Stats", True, (0, 0, 0))
        self.screen.blit(text_stats, (270, 150))

    def _draw_stats(self):
        text_back = self.font.render("Back", True, (0, 0, 0))
        self.screen.blit(text_back, (5, 10))
        wins = self.repo.get_win_amound()
        loses = self.repo.get_lost_amound()
        text_wins_loses = self.font.render("won/lost", True, (0, 0, 0))
        self.screen.blit(text_wins_loses, (270, 100))
        color = (0, 0, 0)  # white
        if wins > loses:
            color = (0, 255, 0)  # green
        elif wins < loses:
            color = (255, 0, 0)  # red
        text_wins_loses_amount = self.font.render(
            f"{wins}/{loses}", True, color)
        self.screen.blit(text_wins_loses_amount, (270, 150))

    def _handle_events_in_stats(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 5 and event.pos[0] < 55 and event.pos[1] > 10 and event.pos[1] < 33:
                    self.view = "menu"

    def _draw_game_over(self):
        if self.game_won:
            text_game_over = self.font.render("You won", True, (0, 0, 0))
        elif not self.game_won:
            text_game_over = self.font.render("You lost", True, (0, 0, 0))
        self.screen.blit(text_game_over, (270, 100))

    def _handle_events_in_game_over(self, event):
        timestamp = datetime.now()
        if self.game_won:
            win_or_loss = "Win"
        else:
            win_or_loss = "Loss"
        self.repo.add_game(timestamp, win_or_loss)
        sleep(4)
        self.view = "menu"
