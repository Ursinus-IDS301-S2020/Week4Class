#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:36:35 2020

@author: ctralie
"""


import numpy as np # This is the main numerical library we will use
import matplotlib.pyplot as plt # This is the main plotting library we will use
import skimage # A library for doing some extra stuff with image processing



# Show aliasing
X = skimage.io.imread("hand-tattoos-hold-man.jpg")
fac = 6
Y = X[0::fac, 0::fac, :]

plt.figure(figsize=(8, 12))
plt.subplot(2, 1, 1)
plt.imshow(X)
plt.title("Original Image")
plt.subplot(2, 1, 2)
plt.imshow(Y)

