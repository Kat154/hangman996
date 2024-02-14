import random 
word_list = ['apple','mango','orange','grapes','pineapple']
print(word_list)

def random_choice(word_list):
    word = random.choice(word_list)
    print(word)
    return word


random_choice(word_list)

def user_input():
    guess = input('please enter a random guess')
    if _is_valid_input(guess):
        print('good guess')
        return guess
    else:
        return 'Oops! That is not a valid input'

def _is_valid_input(guess):
    if len(guess) == 1:
        all_alphabets = 'abcdefghijklmnopqrstuvwxyz' 
        if guess.lower() in all_alphabets:
            return True 
    else:
        return False 
