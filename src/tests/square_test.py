import unittest
from ent_square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square()
    def test_square_flag_turns_to_true(self):
        self.square.flagging()
        self.assertEqual(self.square.flag, True)
