# Create a Boggle Simulator
# Intended to be used by a single player
# Will have 16 dice each with a specific set of letters on them

from random import shuffle
from random import choice
import numpy as np

class BoggleGame():
    def __init__(self):
        self.dice = [['A','E','A','N','E','G'],
               ['A','H','S','P','C','O'],
               ['A','S','P','F','F','K'],
               ['O','B','J','O','A','B'],
               ['I','O','T','M','U','C'],
               ['R','Y','V','D','E','L'],
               ['L','R','E','I','X','D'],
               ['E','I','U','N','E','S'],
               ['W','N','G','E','E','H'],
               ['L','N','H','N','R','Z'],
               ['T','S','T','I','Y','D'],
               ['O','W','T','O','A','T'],
               ['E','R','T','T','Y','L'],
               ['T','O','E','S','S','I'],
               ['T','E','R','W','H','V'],
               ['N','U','I','H','M','Qu']]

    def start_game(self):
        
        shuffle(self.dice)
        rows = []
        for i in range(4):
            new_row = [choice(self.dice[i*4 + 0]),
                        choice(self.dice[i*4 + 1]),
                        choice(self.dice[i*4 + 2]),
                        choice(self.dice[i*4 + 3])]
            rows.append(new_row)
        game_letters =[]
        for row in rows:
            print(*row, sep = " ")
            game_letters.append(row)
        return game_letters
            

    def welcome_sign(self):
        print("Welcome to Boggle!")

    def get_user_word(self):
        print("Type a word and press enter or press X to exit the game and receive your score: ")
        self.word = input()
        return self.word
 
    def import_file(filename:str):
        pass
    
    def is_word_three_letters(self,word):
        if len(word) >= 3:
            return True
        else:
            return False

    def get_list_of_letters(self, game_letters):
        game_letters_list = []
        for row in game_letters:
            for element in row:
                game_letters_list.append(element)
        return game_letters_list

    def is_word_on_board(self, word:str, game_letters_list:list) -> bool:
        lowercase_letters = [each_letter.lower() for each_letter in game_letters_list]
        count = 0
        for letter in word:
            if letter in lowercase_letters:
                count += 1
            else:
                return False
        if count == len(word):
            return True      

    # will check if the word is made using adjacent letters
    def is_word_valid(self):
        pass

    def was_letter_used_twice(**kwargs) -> bool:
        pass
    
    def get_score(self, list_of_valid_words):
        total = 0
        for i in list_of_valid_words:
            print(len(i))
            if len(i) == 3 or len(i) == 4:
                total += 1
            elif len(i) == 5:
                total += 2
            elif len(i) == 6:
                total += 3
            elif len(i) == 7:
                total += 5
            elif len(i) >= 8:
                total += 11
        count = len(list_of_valid_words)
        return count,total

def main():
        word = " "
        bg = BoggleGame()
        bg.welcome_sign()
        game_letters = bg.start_game() # returns a 2d array
        list_of_valid_words = []
        while True:
            game_letters_list = bg.get_list_of_letters(game_letters) # returns a string list 
            word = bg.get_user_word()
            if word.lower() == "x":
                if len(list_of_valid_words) == 0:
                    print("Your score is 0.")
                    break
                else:
                    count, score = bg.get_score(list_of_valid_words)
                    print("Game over.")
                    print("You got " + str(count) + " words!")
                    print("Your total score is: " + str(score) + " points!")
                    break
            else:
                # check to see if the word is three letters or more
                word_is_three_letters = bg.is_word_three_letters(word.lower())
                # check to see if letters are even on the board
                word_on_board = bg.is_word_on_board(word.lower(), game_letters_list)
                if word_on_board  & word_is_three_letters:
                    list_of_valid_words.append(word.lower())
                else:
                    print("Word is not valid.")
            

main()



