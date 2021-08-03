# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:44:28 2020

@author: SIU851463587
"""
'''
This creates a chemical formula with subscript numbers with an
input of letters and regular typed numbers'''

def chemical_formula(x:str):
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    print(x.translate(sub))
    
chemical_formula("C5H12O")


