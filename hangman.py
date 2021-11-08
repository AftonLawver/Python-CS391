'''
Author: Afton Lawver
'''
# Tips:
# Create a function that displays word if user wants to give up

# Steps
# 1. Import word list txt file ✔
# 2. Choose secret word from imported file ✔
# 3. Display to the user: Your word has X letters ✔ 
# 4. Have player guess one letter ✔
# 5. Check to see if there are any occurrences of that letter in secret word ✔
# 6. If there are occurrences of that letter fill in the blank with that letter ✔ 
# 7. Display to the user: Guess another letter, here is your word so far.. ✔
# 8. Make sure no double guesses are allowed

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

def is_letter_in_word(letter:str, word:str):
    if letter in word:
        return True
    else:
        return False

def was_letter_already_guessed(list_of_guessed_letters:list, letter:str):
    pass

def list_to_str(input_list:list):
    string = ' '.join(input_list)
    return string

def string_to_list(string:str):
    my_list = ["_" for element in string]
    return my_list

def occurrences_of_letter_in_word(letter:str, my_string:str):
    if letter.upper() in my_string:
        return True
    else:
        return False

def find_index_and_replace(letter:str, my_string:str, list_to_modify:list):
    my_list = [element for element in my_string]
    for i, element in enumerate(my_list):
        if element == letter:
            list_to_modify[i] = letter
    new_string = list_to_str(list_to_modify)
    return new_string

def was_letter_guessed_before(letter:str, list_of_letters_chosen:list):
    if letter in list_of_letters_chosen:
        return True
    else:
        return False

def are_all_letters_filled_in(my_word:str):
    # my_list = [element for element in my_word]
    my_list = [x for x in my_word if x != " "]
    if "_" in my_list:
        return False
    else:
        return True

def guessed_word_right(guessed_word:str, game_word:str):
    if guessed_word == game_word:
        return True
    else:
        return False

letters_chosen = []
guess_word = []
guesses = 0
word = choose_secret_word()
play = int(input("Welcome to Hangman! Press 1 to play or 0 to exit the game."))
if play == 1:
    my_list = string_to_list(word)
    my_string = list_to_str(my_list)
    print(my_string)
    while True:
        if guesses == 0:
            chosen_letter = input("Guess any letter. \nOr type 2 to guess the word.").upper()     
            if chosen_letter.isalpha():  # to make sure the letter guessed is actually a letter.
                if was_letter_guessed_before(chosen_letter, letters_chosen) == False:
                    letters_chosen.append(chosen_letter)
                    if occurrences_of_letter_in_word(chosen_letter, word):
                        print("Good job. That letter is in the word.")
                        # find the index(es) of the guessed letter and replace the _ _ _ _ _ string with that guessed letter
                        new_word = find_index_and_replace(chosen_letter, word, my_list)
                        print(new_word)
                        guesses += 1
                        if are_all_letters_filled_in(new_word):
                            print("Congratulations, it took you {} guesses to figure out the word {}".format(guesses, new_word))
                            break
                        else:
                            continue
                    else:
                        print("Letter not in word.")
                        guesses += 1
                        print(new_word)
                        continue   
                else:
                    print("Letter was guessed already.") 
                    print(new_word)
                    continue            
            else:
                chosen_letter = int(chosen_letter)
                if chosen_letter == 2:
                    guess_word = input("Type your guess: ")
                    if guessed_word_right(guess_word, word):
                        print("Congratulations, you won in one guess!")
                    else:
                        print("That is incorrect.")
                        guesses += 1
                        print(new_word)
                else:
                    print("Enter a valid letter.")
                    continue
        else:
            chosen_letter = input("Guess another letter. \n").upper()     
            if chosen_letter.isalpha():  # to make sure the letter guessed is actually a letter.
                if was_letter_guessed_before(chosen_letter, letters_chosen) == False:
                    letters_chosen.append(chosen_letter)
                    if occurrences_of_letter_in_word(chosen_letter, word):
                        print("Letter is in word.")
                        # find the index(es) of the guessed letter and replace the _ _ _ _ _ string with that guessed letter
                        new_word = find_index_and_replace(chosen_letter, word, my_list)
                        print(new_word)
                        guesses += 1
                        if are_all_letters_filled_in(new_word):
                            print("Congratulations, it took you {} guesses to figure out the word {}".format(guesses, new_word))
                            break
                        else:
                            continue
                    else:
                        print("Letter not in word.")
                        guesses += 1
                        print(new_word)
                        continue   
                else:
                    print("Letter was guessed already.") 
                    print(new_word)
                    continue            
            else:
                print("Enter a valid letter.")
                continue    
elif play == 0:
    print("Game exited.")