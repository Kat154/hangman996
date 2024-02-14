import random

class Hangman:
	def __init__(self,word_list,num_lives=5):
		self.word = random.choice(word_list)
		self.word_guessed = ['_' for i in range(len(self.word))]
		self.word_list = word_list
		self.num_lives = num_lives
		
		self.list_of_guesses = []

	def check_guess(self,guess):
		if guess.lower() in self.word:
			print(f'Good guess! {guess} is in the word.')
			for index in range(len(self.word)):
				if self.word[index] == guess and self.word_guessed[index]== '_':
					self.word_guessed[index].replace(guess)
			num_lives -= 1
		else:
			num_lives -= 1
			print(f'sorry, {guess} is not in the word')
			print(f'you have {num_lives} lives left')


	def ask_for_input(self):
		while True:
			guess = input('please guess: ')
			if not len(guess) == 1 and guess.isaplha():
				print(f'Invalid letter. Please, enter a single alphabetical character.')
			elif guess in self.list_of_guesses:
				print(f'you already tried that letter')
			else:
				check_guess(guess)
				list_of_guesses.append(guess)

if __name__ == '__main__':
	pass 
