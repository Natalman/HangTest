import unittest

from unittest.mock import patch
from Hangman import hangman

class TestGame (unittest.TestCase):

    @patch('random.randint', return_value = "poetry")
    def test_choice(self, mock_random):
        words = "cotton"
        self.assertTrue("poetry", hangman.random_choice(words))

    @patch ('builtins.input', side_effect = ['c', 'm', 'v', 'o', 't'])
    @patch ('builtins.print')
    def test_user_input(self, mock_print, mock_input):
        self.assertTrue('c', hangman.user_input())
        self.assertTrue('m', hangman.user_input())

    def get_file_text(self):
        textToWrite = "This line"
        return textToWrite

    def test_read_file(self):
        self.assertTrue(self.get_file_text,hangman.read_text())
