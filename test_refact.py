import unittest
import random

from refact import Hangman
import difficulty_settings
from graphics import HangmanGraphics


class RefactTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing environment"""
		self.game = Hangman()
		self.easy = EasyMode()
		self.medium = MediiumMode()
		self.hard = HardMode()
		self.graphics = HangmanGraphics()

	def tearDown(self):
		"""Tear down the testing environment"""
		self.game = None
		self.easy = None
		self.medium = None
		self.hard = None
		self.graphics = None

	def test_rand_word_gen(self):
		"""Test that the secret word is converted into underscores and coverted to string"""
		secret_word = 'test'
		blank_word = len(secret_word) * '_'
		blank_word = list(blank_word)
		blank_word = ''.join(blank_word)
		self.assertTrue(Hangman.gen_blank_word(secret_word) == blank_word)

if __name__ == '__main__':
	unittest.main()