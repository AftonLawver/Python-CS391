# Create a Boggle Simulator
# Intended to be used by a single player
# Will have 16 dice each with a specific set of letters on them

import random
import numpy as np






class Array2D():
   def __init__(self, *letters:list):
       if len(letters) > 0:
           for a in letters:
               if isinstance(a, list) == False:
                   raise Exception("Invalid type argument")
           self.__arr__ = [ a for a in letters ]
       else:
           raise Exception("Invalid number of arguments")

   def append_row(self, letters:list):
       if isinstance(letters, list) == False:
           raise Exception("Invalid type argument")
       self.__arr__.append(letters)

   def display(self):
       print(len(self.__arr__[0][0]) * 2 * " ", end="")
       [print(i, end=" ") for i in range(0,len(self.__arr__[0]))]
       print()
       for row_index,row in enumerate(self.__arr__):
           print(row_index, end=" ")
           for element in row:
               print(element,end=" ")
           print()
       print(len(self.__arr__[0][0]) * 2 * " ", end="")

   def __call__(self):
       return self.__arr__

a = Array2D(['I','O','T','M','U','C'],['R','Y','V','D','E','L'])
a.append_row(['A','H','S','P','C','O'])
print(a.display())

# Dice class will be used to create the 16 different dice
class Dice:
    def __init__(self, sides:list):
        self.sides = sides

    def roll_dice(self):
        x = random.choice(self.sides)
        return x


def create_array(letters:list):
    shuffled_list = random.sample(letters, len(letters))
    letters1 = shuffled_list[0:4]
    letters2 = shuffled_list[4:8]
    letters3 = shuffled_list[8:12]
    letters4 = shuffled_list[12:16]
    arr = [letters1, letters2, letters3, letters4]
    print(arr)
    return arr

def show_array_to_user(arr:list):
    for i in arr:
        for j in i:
            print(j, end = " ")
        print()
    

def main():

    dice1 = Dice(['A','E','A','N','E','G'])
    letter1 = dice1.roll_dice()
    print(letter1)

    dice2 = Dice(['A','H','S','P','C','O'])
    letter2 = dice2.roll_dice()
    print(letter2)

    dice3 = Dice(['A','S','P','F','F','K'])
    letter3 = dice3.roll_dice()
    print(letter3)

    dice4 = Dice(['O','B','J','O','A','B'])
    letter4 = dice4.roll_dice()
    print(letter4)

    dice5 = Dice(['I','O','T','M','U','C'])
    letter5 = dice5.roll_dice()
    print(letter5)

    dice6 = Dice(['R','Y','V','D','E','L'])
    letter6 = dice6.roll_dice()
    print(letter6)

    dice7 = Dice(['L','R','E','I','X','D'])
    letter7 = dice7.roll_dice()
    print(letter7)

    dice8 = Dice(['E','I','U','N','E','S'])
    letter8 = dice8.roll_dice()
    print(letter8)

    dice9 = Dice(['W','N','G','E','E','H'])
    letter9 = dice9.roll_dice()
    print(letter9)

    dice10 = Dice(['L','N','H','N','R','Z'])
    letter10 = dice10.roll_dice()
    print(letter10)

    dice11 = Dice(['T','S','T','I','Y','D'])
    letter11 = dice11.roll_dice()
    print(letter11)

    dice12 = Dice(['O','W','T','O','A','T'])
    letter12 = dice12.roll_dice()
    print(letter12)

    dice13 = Dice(['E','R','T','T','Y','L'])
    letter13 = dice13.roll_dice()
    print(letter13)

    dice14 = Dice(['T','O','E','S','S','I'])
    letter14 = dice14.roll_dice()
    print(letter14)

    dice15 = Dice(['T','E','R','W','H','V'])
    letter15 = dice15.roll_dice()
    print(letter15)

    dice16 = Dice(['N','U','I','H','M','Qu'])
    letter16 = dice16.roll_dice()
    print(letter16)

    list_of_letters = [letter1, letter2, letter3, letter4, letter5, letter6, letter7, letter8, letter9, letter10, letter11, letter12, letter13, letter14, letter15, letter16]

    
    x = create_array(list_of_letters)
    show_array_to_user(x)
    
    

    

main()

