#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:46:26 2020

@author: ctralie
"""

# TODO: Try inputting 9, and see if you can figure
# out what the bug is (hint: we need elif)

def get_damage(richter):
    """
    Given a measurement on the richter scale, print out
    information about the damage to expect
    NOTE: This is a buggy method for educational purposes
    Parameters
    ----------
    richter: float
        A measurement on the richter scale
    """
    if richter >= 8:
        print("Everything collapses")
    if richter >= 7:
        print("Many collapse")
    if richter >= 6:
        print("Many damaged")
    if richter >= 4.5:
        print("Only poorly constructed damaged")
    else:
        print("We're cool")

print("Input richter: ")
get_damage(float(input()))