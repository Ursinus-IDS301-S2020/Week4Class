#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:46:56 2020

@author: ctralie
"""
import numpy as np
import matplotlib.pyplot as plt

def plot_circle(n_points):
    """
    Plot some points evenly sampled on a circle
    Paramters
    ---------
    n_points: int
        The number of points to draw between 0 and 2PI, inclusive
    """
    ## Step 1: Setup a 1D array with all of the angles we want 
    ## to sample
    theta = np.linspace(0, 2*np.pi, n_points)
    ## Step 2: Setup a 2D array that will hold all of the samples
    ## The first column will hold the x coordinates, and the second
    ## column will hold the y coordinates
    X = np.zeros((n_points, 2))
    ## Step 3: Loop through and fill in one row at a time
    for i in range(n_points):
        X[i, 0] = np.cos(theta[i])
        X[i, 1] = np.sin(theta[i])
    ## Step 4: Plot the first column as the x-coordinate and the
    ## second column as the y-coordinate
    plt.plot(X[:, 0], X[:, 1])

plot_circle(20)