#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:46:26 2020

@author: ctralie
"""

def get_damage(richter):
    """
    Given a measurement on the richter scale, print out
    information about the damage to expect
    Parameters
    ----------
    richter: float
        A measurement on the richter scale
    """
    if richter >= 8:
        print("Everything collapses")
    elif richter >= 7:
        print("Many collapse")
    elif richter >= 6:
        print("Many damaged")
    elif richter >= 4.5:
        print("Only poorly constructed damaged")
    else:
        print("We're cool")

print("Input richter: ")
richter_in = float(input())
get_damage(richter_in)