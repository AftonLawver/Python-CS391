# Create a Boggle Simulator
# Intended to be used by a single player
# Will have 16 dice each with a specific set of letters on them


import random
import copy

class BoggleGame():
   def __init__(self, *args):
       dice = Array2D(*args)
       temp = {}
       self.grid = [[dice()[random.randint(0,5)] for _ in range(0,4)] for _ in range(0,4)]
       for row_index, row in enumerate(self.grid):
           for column_index, column in enumerate(row):
               temp[(row_index, column_index)] = column
       self.grid = copy.deepcopy(temp)
       
   def find_all_letters(self, letter:str):
       letters_found = {}
       for key,value in self.grid.items():
           if value == letter:
               letters_found[key] = value
       return letters_found

   def import_file(filename:str):
       pass

   def is_word_in_grid(word:str) -> bool:
       # example afton
       for letter in word:
           pass

   def was_letter_used_twice(**kwargs) -> bool:
       pass
class Array2D():
   def __init__(self, *letters:list):
       self.current_index_row = 0
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
       row = self.__arr__[self.current_index_row]
       self.current_index_row +=1
       return row
bg = BoggleGame(['A','E','A','N','E','G'],
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
               ['N','U','I','H','M','Qu'] )

