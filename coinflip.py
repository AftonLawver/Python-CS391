# Class that simulates a coin flipping
import random
import os
print(os.getcwd())

class Coin:

    def __init__(self):
        self.__side_up = "Heads"

    def flip_coin(self):
        x = random.randint(0,1)
        if x == 0: 
            self.__side_up = "Tails"
        else: 
            self.__side_up = "Heads"
        
    def get_side_up(self):
        return self.__side_up
        


coin1 = Coin()
num_tails = 0
num_heads = 0

for i in range(0,10000):
    coin1.flip_coin()
    side = coin1.get_side_up()
    if side == "Heads":
        num_heads += 1
    elif side == "Tails":
        num_tails += 1
print("Number of Heads: {}".format(num_heads))
print("Number of Tails: {}".format(num_tails))



    
