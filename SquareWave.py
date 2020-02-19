#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:41:53 2020

@author: ctralie
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
f = 4
y = np.sin(2*np.pi*f*t)
n_harmonics = 100
for i in range(1, n_harmonics+1):
    k = i*2 + 1
    y = y + np.sin(2*np.pi*f*k*t)/k
plt.plot(t, y)