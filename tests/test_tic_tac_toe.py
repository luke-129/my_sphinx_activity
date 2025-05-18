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

    def test_is_win_diagonal(self):

        for n in range(3):
            self.board[n][n] = "X"

        self.assertTrue(is_win("X", self.board), "is_win is not detecting a diagonal win.")

    def test_is_win_horizontal(self):

        self.board[0][0] = "X"
        self.board[0][1] = "X"
        self.board[0][2] = "X"

        self.assertTrue(is_win("X", self.board), "is_win is not detecting a horizontal win.")

    def test_is_win_vertical(self):
        self.board[0][0] = "X"
        self.board[1][0] = "X"
        self.board[2][0] = "X"

        self.assertTrue(is_win("X", self.board), "is_win is not detecting a vertical win.")

    def test_tally_wins(self):
        wins = (0, 2, 5, 1, 5, 0)

        result = tally_wins(wins)

        self.assertEqual(result, 13)





