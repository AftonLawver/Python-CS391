'''
Author: Afton Lawver
'''
# Tips:
# Create a function that displays word if user wants to give up

# Steps
# 1. Import word list txt file
# 2. Choose secret word from imported file
# 3. Display to the user: Your word has X letters
# 4. Have player guess one letter
# 5. Check to see if there are any occurrences of that letter in secret word
# 6. If there are occurrences of that letter fill in the blank with that letter.
# 7. Display to the user: Guess another letter, here is your word so far..
# 8. 

import random


number_of_guesses = 0

def import_word_list():
    my_word_list = []
    with open('word_list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            my_word_list.append(line)
        my_word_list = [s.replace("\n", "") for s in my_word_list]
    return my_word_list

def choose_secret_word():
    x = import_word_list()
    secret_word = random.choice(x)
    return secret_word


word = choose_secret_word()
print(word)