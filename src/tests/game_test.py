import unittest
from logic.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game_with_full_board = Game(225, 15)
        self.game_with_empty_board = Game(0, 15)
    def test_board_is_correct_width(self):
        self.assertEqual(self.game.size, len(self.game.board[0]))
    def test_board_is_correct_hight(self):
        self.assertEqual(self.game.size, len(self.game.board))
    def test_board_has_correct_amount_of_bombs(self):
        bomb_count = 0
        for row in self.game.board:
            for block in row:
                if block.bomb:
                    bomb_count += 1
        self.assertEqual(self.game.bombs, bomb_count)
    def test_handles_rightclick(self):
        self.game.handle_rightclick_on_board(4, 6)
        self.assertEqual(True, self.game.board[6][4].flag)
    def test_handles_leftclick_on_board_if_bomb(self):
        self.assertEqual(self.game_with_full_board.handle_leftclick_on_board(0, 6), False)
    def test_count_bombs(self):
        self.game_with_full_board._count_bombs_around_block(0, 0)
        self.assertEqual(self.game_with_full_board.board[0][0].bombs_around, 3)
        self.game_with_full_board._count_bombs_around_block(14, 0)
        self.assertEqual(self.game_with_full_board.board[0][14].bombs_around, 3)
        self.game_with_full_board._count_bombs_around_block(0, 14)
        self.assertEqual(self.game_with_full_board.board[14][0].bombs_around, 3)
        self.game_with_full_board._count_bombs_around_block(14, 14)
        self.assertEqual(self.game_with_full_board.board[14][14].bombs_around, 3)
    def test_handles_leftclick_on_board_if_not_bomb(self):
        self.assertEqual(self.game_with_empty_board.handle_leftclick_on_board(5, 7), True)

        
