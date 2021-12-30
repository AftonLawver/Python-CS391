# how to import a module
# module must be saved in same location
import os
import coinflip
from coinflip import Coin

print(coinflip.__file__)
coin_1 = Coin()
for i in range(0,10):
    coin_1.flip_coin()
    x = coin_1.get_side_up()
    print(x)







