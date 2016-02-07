"""Welcome to mystery word, a game that replicates hangman where
players try to guess what the secret word is before they are hanged.


Author: Joseph Moran
Created: 02/06/2016

#!usr/local/bin/env python3.5
"""
from nltk.tokenize import RegexpTokenizer
import random
import math
import sys
import os

import difficulty_settings


class Hangman:


	def __init__(self):
		"""initialize variables"""
		pass

	def gen_rand_word(self, min_letter, max_letter):
		"""Generate a random word from the words file on the pc"""
		with open('/usr/share/dict/words') as f:
			text = f.read()
			tokenizer = RegexpTokenizer(r'\w+')
			content = tokenizer.tokenize(text)
			words = [word.lower() for word in content if min_letter <= len(word) <= max_letter]
			word = random.choice(words)
			return word

	def gen_blank_word(self, secret_word):
		"""Hide the secret word with underscores and give spacing between each underscore"""
		blank_word = len(secret_word) * '_'
		blank_word = list(blank_word)
		blank_word = ''.join(blank_word)
		return blank_word

	def user_try(self):
		"""Have user guess a letter"""
		print(self.display_info(self.blank_word))
		guess = input("\nGuess a letter ")
		return [guess, self.blank_word]
		
	def check_try(self, guess, secret_word, bad_guesses, blank_word):
		"""Check if the user guess was right or wrong"""
		good_guesses = list(self.secret_word)
		if guess in good_guesses:
			return self.correct_guess(guess, self.secret_word, self.blank_word)
		elif guess == '':
			return self.nothing_guessed()
		elif not guess.isalpha():
			return self.not_letter()
		elif guess in self.bad_guesses:
			return self.same_letter_guess()
		elif guess not in good_guesses:
			return self.incorrect_guess(self.bad_guesses, guess)

	def correct_guess(self, guess, secret_word, blank_word):
		"""Inform player has guessed a correct letter"""
		self.clear()
		print("You guessed a correct letter!")
		self.blank_word = list(self.blank_word)
		self.blank_word = self.place_correct_letter(guess, self.secret_word, self.blank_word)
		self.blank_word = ''.join(self.blank_word)
		return self.blank_word

	def place_correct_letter(self, guess, secret_word, blank_word):
		"""Replace underscore with the letter guessed"""
		for index, letter in enumerate(self.secret_word):
			if letter == guess:
				self.blank_word[index] = guess
		if '_' not in self.blank_word:
			return self.game_over_win(self.secret_word)
		else:
			return self.blank_word

	def incorrect_guess(self, bad_guesses, guess):
		"""Tell user their guess was incorrect"""
		self.clear()
		print("That is not a letter in the secret word")
		self.guesses += 1
		self.bad_guesses.append(guess)
		return self.bad_guesses

	def not_letter(self):
		"""Display that the player has typed an invalid character and have them try again"""
		self.clear()
		print("That is not letter! Try again.")
		return self.user_try()

	def same_letter_guess(self):
		"""Display the player has already guessed that word!"""
		self.clear()
		print("You have already guessed that letter! Try again.")
		return self.user_try()

	def nothing_guessed(self):
		"""Display the player typed nothing"""
		self.clear()
		print("You did not type anything! Try again.")
		return self.user_try()

	def game_over_win(self, secret_word):
		"""The game is over and the player won"""
		print("You won the game! The word was {}".format(self.secret_word))
		return sys.exit()

	'''def play_again(self):
		"""Ask the player if they want to play again"""
		again = input("Do you want to play again? Y/n ")
		if again != 'n':
			return player=input("What is your name player? "))
		else:
			return sys.exit()'''

	def game_over_lose(self, secret_word):
		"""The game is over and the player lost"""
		print("You lost! The secret_word was {}".format(secret_word))
		return sys.exit()

	def display_info(self, blank_word):
		"""Display blank word and guesses already picked"""
		print("\nThe word is {} characters long\n".format(len(self.blank_word)))
		print(self.secret_word)
		print("{}\n\n".format(self.blank_word))
		for letter in self.bad_guesses:
			print('{}'.format(letter), end=' ')

	def clear(self):
		"""Clear the screen for easier readability"""
		if os.name == 'nt':
			return os.system('cls')
		else:
			return os.system('clear')

	def setup(self, difficulty):
		"""Select which game environment to start up"""
		if difficulty == 'e':
			game = difficulty_settings.EasyMode(player=input("What is your name player? "))
			game.round()
		elif difficulty == 'm':
			game = difficulty_settings.MediumMode(player=input("What is your name player? "))
			game.round()
		elif difficulty == 'h':
			game = difficulty_settings.HardMode(player=input("What is your name player? "))
			game.round()
		elif difficulty not in 'emh':
			print("That is not a valid difficulty. Try again.\n")

	def round(self):
		"""Create a round of the game"""
		while self.guesses < 7:
			self.play()
		else:
			self.game_over_lose(self.secret_word)

	def play(self):
		"""Start the game"""
		user_guess = self.user_try()
		right_or_wrong = self.check_try(user_guess[0], self.secret_word, self.bad_guesses, user_guess[1])
		return

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	while True:
		game = Hangman()
		difficulty = input("What difficulty do you want to play? "
					   "[E]asy? [M]edium? or [H]ard? Pick a letter "
					   "in the brackets. ").lower()
		game.setup(difficulty)