import random
import math
'''
# Method that randomly generates a number between 0 and 100 
# Returns true if number is divisible by 3, and false otherwise.
def rand_divis_3():
    x = random.randint(0,100)
    if x % 3 == 0: 
        return x, True
    else:
        return x, False

print(rand_divis_3())
'''

'''
# Method called roll_dice that takes two parameters:
# number of sides on dice, and the number of dice.
# This method randomly generates a random number for 
# each die and prints it. Then once that is complete
# it returns That's all. 
def roll_dice(sides:int, num_dice:int):
    for dice in range(num_dice):
        print(random.randint(1,sides))
    return "That's all!"

print(roll_dice(6,3))
'''

# List comprehensions
'''
newlist = [x*x for x in list(range(1,11))]
print(newlist)
'''

'''
# Using the escape sequence.
print("Produces \n\t this \n\t\t output.")
'''


# Produce a multiplication table and encapsulate it within another function

'''
def print_multiples(n:int, high):
    i = 1
    while i <= high:
        print(n*i, end = "\t")
        i += 1
    print()

def print_mult_table(high:int):
    n = 1
    while n <= high:
        print_multiples(n, high)
        n += 1
    
print_mult_table(5)

'''

# Function that finds the index of a character in a string
'''
def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return "{} is at index position {} in the string {}".format(ch, index, str)
        index += 1
    return -1

print(find("Produces", 'd'))
'''
'''
# Function that counts specific letters in a string
# Both the letters/character(s) and the string are passed in
# as an arguments.
def count_letters(str, ch):
    word = str
    count = 0
    for char in word:
        if char == ch:
            count += 1
    if count == 0:
        return "There are no {}'s in '{}'".format(ch, word)
    if count == 1:
        return "There is 1 {} in '{}'".format(ch, word)
    else:
        return "There are {} {}'s in '{}'".format(count, ch, word)
       
print(count_letters("Hello world.", 'l'))

'''

'''
# Loop that traverses a list and prints the length of each element
# Note: len() does not work with int
my_list = ["Afton", "John", "firefighter"] 
for i in my_list:
    print("{}: {}".format(i, len(i)))
'''

