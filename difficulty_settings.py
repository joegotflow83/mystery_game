from refact import Hangman


class EasyMode(Hangman):
	"""Create an environment for the player to play on easy mode"""

	def __init__(self, player):
		"""Initialize variables"""
		self.player = player
		self.guesses = 0
		self.bad_guesses = []
		self.secret_word = Hangman.gen_rand_word(self, 4, 6)
		self.blank_word = Hangman.gen_blank_word(self, self.secret_word)


class MediumMode(Hangman):
	"""Create an environment for the player to play on medium mode"""

	def __init__(self, player):
		"""Initialize variables"""
		self.player = player
		self.guesses = 0
		self.bad_guesses = []
		self.secret_word = Hangman.gen_rand_word(self, 6, 10)
		self.blank_word = Hangman.gen_blank_word(slef, self.secret_word)


class HardMode(Hangman):
	"""Create an environment for the player to play on hard mode"""

	def __init__(self, player):
		"""Initialize variables"""
		self.player = player
		self.guesses = 0
		self.bad_guesses = []
		self.secret_word = Hangman.gen_rand_word(self, 10, 100)
		self.blank_word = Hangman.gen_blank_word(self, self.secret_word)