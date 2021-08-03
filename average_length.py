# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 07:17:29 2020

Lead Programmer: Afton Lawver
"""

# Simple Algorithms

# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

def average_Length(sentence:str):
    
    for p in "!?'.,:;":
        sentence = sentence.replace(p, "")
    
    words = sentence.split(' ')
    return round(sum(len(word)for word in words)/ len(words), 2)
    
print(average_Length("Hello, my name is Afton"))