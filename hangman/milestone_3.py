
import random 
word_list = ['apple','mango','orange','grapes','pineapple']
print(word_list)

def random_choice(word_list):
    word = random.choice(word_list)
    print(word)
    return word


random_choice(word_list)

def ask_for_input():
	while True:
		guess = input('please enter a guess:  ')
		if guess.isalpha() and len(guess)==1:
			break
		else:
			print('Invalid letter. Please, enter a single alphabetical character.')
	word = random.choice(word_list)

def check_guess(guess):
	if guess in word:
		f'Good guess! {guess} is in the word.'
		return True
	else:
		f'Sorry, {guess} is not in the word. Try again.'
		return False

ask_for_input()