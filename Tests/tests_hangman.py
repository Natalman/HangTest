import unittest

from unittest.mock import patch
from Hangman import hangman

class TestGame (unittest.TestCase):

    @patch('random.randint', return_value = "poetry")
    def test_choice(self, mock_random):
        words = "cotton"
        self.assertTrue("poetry", hangman.random_choice(words))


    def get_file_text(self):
        self.textToWrite = 'word'
        return textToWrite

    def test_read_file(self):
        self.assertTrue(self.get_file_text,hangman.read_text())


    def test_game_on(self):

        self.assertTrue(hangman.Game_on(5, ['c', '',  't'] , ['c', 'a', 't']))
        self.assertFalse(hangman.Game_on(6, ['c', '',  't'] , ['c', 'a', 't']))
        self.assertFalse(hangman.Game_on(5, ['c', 'a',  't'] , ['c', 'a', 't']))





    @patch ('builtins.input', side_effect = ['c', 'm', 'v', 'o', 't'])
    @patch ('builtins.print')
    def test_user_input(self, mock_print, mock_input):
        self.assertTrue('c', hangman.user_input())
        self.assertTrue('m', hangman.user_input())

    @patch('Hangman.hangman.user_input', return_value = 'p')
    def test_right_guess(self, mock_guess):
        self.assertFalse(hangman.user_input())

    @patch('Hangman.hangman.user_input', return_value = 'i')
    def test_right_guess(self, mock_guess):
        self.assertTrue(hangman.user_input())

    @patch('Hangman.hangman.user_input', return_value = 'p')
    @patch('builtins.print')
    def test_main_user_wins(self, mock_print, mock_guess):

        hangman.main()

        mock_print.assert_any_call('Right guess!!!')
