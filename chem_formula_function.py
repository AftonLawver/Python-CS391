# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:44:28 2020

@author: Afton Lawver
"""

def chemical_formula(chemical_formula:str):
    """Changes all numbers in a chemical formula from 
    regular-sized numbers to subscript.

    Args:
        chemical_formula (str): Chemical formula without subscript 
        numbers. 
    """
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    print(chemical_formula.translate(sub))
    
chemical_formula("C5H12O")
