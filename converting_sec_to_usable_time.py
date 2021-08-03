# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:12:49 2020

@author: SIU851463587
"""

def seconds(x:int):
    d = x//86400
    h = x % 86400 // 3600
    m = x % 86400 % 3600 // 60
    s = x % 60 
    print(f'days:{d:02} hours:{h:02} min:{m:02} sec:{s:02}')
    
seconds(100) 