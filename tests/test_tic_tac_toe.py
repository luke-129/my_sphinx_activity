from src.tic_tac_toe import print_board, is_win, tally_wins
from unittest import TestCase


class TestGame(TestCase):
    def setUp(self):
        self.board = [[' ' for _ in range(3)]for _ in range(3)]
        self.layout = []

        for row in self.board:
            self.layout.append('|'.join(row))
            self.layout.append('-' * 5)
        self.board_string = '\n'.join(self.layout)

    def test_print_board(self):
        print_board()
        self.assertEqual(print_board(), self.board_string)

    def test_is_win(self):
        ...

    def test_tally_wins(self):
        ...




