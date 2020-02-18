#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:29:55 2020

@author: ctralie
"""

def get_elevator_floor(actual_floor):
    """
    Given an actual floor, convert it to an elevator
    button number by skipping the thirteenth floor
    Parameters
    ----------
    actual_floor: int
        The actual floor we're traveling to

    Returns
    ----------
    elevator_floor: int
        What the elevator button says
    """
    if actual_floor >= 13:
        elevator_floor = actual_floor + 1
    return elevator_floor

print("Input floor")
floor = int(input())
print("Elevator Floor: ", get_elevator_floor(floor))