import unittest
from unittest.mock import patch
from board import Board  # Assuming your main class is named 'Board'

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        # Check if the board is initialized correctly
        self.assertEqual(len(self.board.squares), 8)
        self.assertEqual(len(self.board.squares[0]), 8)

    def test_move(self):
        # Mock input for a move
        move_mock = patch('builtins.input', return_value="e2 e4")

        with move_mock:
            # Perform a move and check if the board is updated
            self.board.move(self.board.squares[6][4].piece, self.board.squares[6][4].piece.moves[0])
            self.assertEqual(self.board.squares[4][4].piece.__class__.__name__, "Pawn")

    def test_valid_move(self):
        # Mock input for a move
        move_mock = patch('builtins.input', return_value="e2 e4")

        with move_mock:
            # Perform a move and check if it is considered valid
            piece = self.board.squares[6][4].piece
            move = self.board.squares[6][4].piece.moves[0]
            self.assertTrue(self.board.valid_move(piece, move))

    def test_check_promotion(self):
        # Mock input for a move resulting in promotion
        move_mock = patch('builtins.input', return_value="e7 e8")

        with move_mock:
            # Perform a move resulting in promotion and check if it is handled correctly
            pawn = self.board.squares[6][4].piece
            move = self.board.squares[6][4].piece.moves[0]
            self.board.move(pawn, move)
            self.assertEqual(self.board.squares[0][4].piece.__class__.__name__, "Queen")



if __name__ == '__main__':
    unittest.main()
