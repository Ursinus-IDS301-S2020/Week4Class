#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:13:50 2020

@author: ctralie

This program shows how to do 
"""

def give_assistance(age, sick):
    """
    Parameters
    ----------
    age: int
        The age of the person
    sick: boolean (True/False)
        Whether the person is sick
    """
    if age > 75 or sick:  #NOTE: You could also write age > 75 or sick == True
        print("I will help you")
    else:
        print("You're on your own")
        
def give_assistance2(age, sick):
    """
    SAME VERSION AS ABOVE, BUT USING DE MORGAN'S LAW TO
    FLIP THE LOGIC AROUND
    Parameters
    ----------
    age: int
        The age of the person
    sick: boolean (True/False)
        Whether the person is sick
    """
    if not (age <= 75 and not sick):
        print("I will help you")
    else:
        print("You're on your own")

give_assistance(70, False)
give_assistance(76, False)
give_assistance(12, True)
give_assistance(31, False)