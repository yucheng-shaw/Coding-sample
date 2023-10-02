#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:44:04 2018

@author: gener
"""

import numpy as np
import scipy.optimize as opt

def func(x):
    value = 0.
    ### START YOUR CODE HERE ###
    value = abs(np.sin(x)/((x/(2*np.pi))**x + np.pi/8)) - x/(2*np.pi) + (x/(2*np.pi))**2 -0.5

    #### END YOUR CODE HERE ####
    return value

def find_all_roots():
    output = np.zeros(5)
    ### START YOUR CODE HERE ###
    output[0] = opt.brenth(func, 0, 1)
    output[1] = opt.brenth(func, 2, 3)
    output[2] = opt.brenth(func, 3, 4)
    output[3] = opt.brenth(func, 5, 6)
    output[4] = opt.brenth(func, 8, 9)
    
    #### END YOUR CODE HERE ####
    return output