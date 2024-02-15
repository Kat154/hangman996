import random

class Hangman:
	def __init__(self,word_list,num_lives=5):
		self.word = random.choice(word_list)
		self.word_guessed = ['_' for i in range(len(self.word))]
		self.word_list = word_list
		self.num_lives = num_lives		
		self.list_of_guesses = []
		self.string_guessed=''

	def check_guess(self,guess):

		if guess.lower() in self.word:
			print(f'Good guess! {guess} is in the word.')
			self._replace_guess_in_word_guessed(guess)
			return True
		else:
			print(f'sorry, {guess} is not in the word')
			print(f'you have {self.num_lives} lives left')
			return False

	def _replace_guess_in_word_guessed(self,guess):
		for index in range(len(self.word)):
			# print(f'came here')
			if self.word[index] == guess and self.word_guessed[index]== '_':
				self.word_guessed[index] = guess


	def ask_for_input(self):
		guess = input('please guess: ')
		while self._is_invalid_input(guess) or self._is_repetetive_guess(guess):	
			if self._is_invalid_input(guess):
				print(f'Invalid letter. Please, enter a single alphabetical character.')
			elif self._is_repetetive_guess(guess):
				print(f'you already tried that letter')
		
		self.num_lives -= 1
		self.list_of_guesses.append(guess)
		print(f'returing guess = {guess} and breaking out of ask_for_input function')
		return guess


	def _is_invalid_input(self,guess):
		if not len(guess) == 1 and guess.isalpha():
			return True 
		else:
			return False 
	def _is_repetetive_guess(self,guess):
		if guess in self.list_of_guesses:
			return True 
		else:
			return False

	def play_game(self):
		while self.num_lives >= 1:
			print(f'self.word = {self.word},self.word_guessed = {self.word_guessed}')
			guess = self.ask_for_input()
			guess_correct = self.check_guess(guess)
			self.string_guessed = ''
			for letter in self.word_guessed:
				self.string_guessed +=letter
			print(f'self.string_guessed: {self.string_guessed}')
			if self.string_guessed == self.word:
				print(f'you have won')
				return f'you have won'

		return f' you have lost, PLease try again'
word_list = ['apple','banana']
game = Hangman(word_list)
game.play_game()



