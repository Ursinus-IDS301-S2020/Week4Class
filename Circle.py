#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:46:56 2020

@author: ctralie
"""

def plot_circle(n_points):
    theta = np.linspace(0, 2*np.pi, n_points)
    X = np.zeros((n_points, 2))
    for i in range(n_points):
        X[i, 0] = np.cos(theta[i])
        X[i, 1] = np.sin(theta[i])
    plt.plot(X[:, 0], X[:, 1])

plot_circle(20)