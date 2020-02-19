#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:35:17 2020

@author: ctralie
"""

x = 0 # Running total of numbers
N = 2000
for i in range(1, N+1):
    x = x + i
print(x)

y = N*(N+1)/2
print(y)