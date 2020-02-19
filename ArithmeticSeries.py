#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:35:17 2020

@author: ctralie

Purpose: To show how to compute an arithmetic series
1 + 2 + ... + N
using a for loop, and comparing that to the formula

N*(N+1)/2

"""

x = 0 # Running total of numbers
N = 2000
for i in range(1, N+1):
    x = x + i
print(x)

y = N*(N+1)/2 # This will be a decimal number, since Python
# adds a decimal when doing division to be safe
print(y)