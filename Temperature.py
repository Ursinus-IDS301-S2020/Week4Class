#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:03:34 2020

@author: ctralie
"""

def check_temperature(temp):
    if temp >= 60 and temp <= 80:
        print("Go outside")
    else:
        print("Stay inside")
        
def check_temperature2(temp):
    """
    THIS IS THE SAME AS ABOVE, BUT THE LOGIC IS FLIPPED
    WITH DEMORGANS
    """
    if not (temp < 60 or temp > 80):
        print("Go outside")
    else:
        print("Stay inside")

check_temperature(75)
check_temperature(55)
check_temperature(82)