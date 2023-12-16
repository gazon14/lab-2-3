import unittest
from unittest.mock import Mock
import pygame
from game import Game  

class TestGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game = Game()

    def test_next_turn(self):
        initial_player = self.game.next_player
        self.game.next_turn()
        new_player = self.game.next_player
        self.assertNotEqual(initial_player, new_player)

    def test_set_hover(self):
        row, col = 2, 3
        self.game.set_hover(row, col)
        self.assertEqual(self.game.hovered_sqr.row, row)
        self.assertEqual(self.game.hovered_sqr.col, col)

    def test_change_theme(self):
        initial_theme = self.game.config.theme
        self.game.change_theme()
        new_theme = self.game.config.theme
        self.assertNotEqual(initial_theme, new_theme)

    def test_play_sound(self):
        # Mocking the sound objects
        self.game.config.capture_sound = Mock()
        self.game.config.move_sound = Mock()

        # Test playing sound for a move
        self.game.play_sound(captured=False)
        self.game.config.move_sound.play.assert_called_once()

        # Test playing sound for a capture
        self.game.play_sound(captured=True)
        self.game.config.capture_sound.play.assert_called_once()

    def test_reset(self):
        initial_player = self.game.next_player
        initial_board = self.game.board
        initial_hovered_sqr = self.game.hovered_sqr
        initial_dragger_piece = self.game.dragger.piece
        initial_config_theme = self.game.config.theme

        self.game.reset()

        self.assertNotEqual(initial_player, self.game.next_player)
        self.assertNotEqual(initial_board, self.game.board)
        self.assertNotEqual(initial_hovered_sqr, self.game.hovered_sqr)
        self.assertNotEqual(initial_dragger_piece, self.game.dragger.piece)
        self.assertNotEqual(initial_config_theme, self.game.config.theme)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
