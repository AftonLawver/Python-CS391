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

