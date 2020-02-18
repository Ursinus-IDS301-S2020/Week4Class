#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:06:27 2020

@author: ctralie
"""

# This program will compute even or odd

def is_even(num):
    """
    Parameters
    ----------
    num: int
        An integer that we want to know is even or odd
    
    Returns
    -------
    result: boolean
        True if it's even, False if it's odd
    """
    result = True
    if num % 2 == 1: # Double == in if statements
        result = False # Single = is assignment
    return result


print("Enter number: ")
x = int(input())
if is_even(x):
    print("Even")
else:
    print("Odd")