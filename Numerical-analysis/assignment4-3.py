#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:01:10 2018

@author: gener
"""

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

nbase = 10000
np.random.seed(1234)
vs = np.hstack((np.random.randn(nbase*3)*0.2+3.,np.random.randn(nbase)*0.6+2.8))
vb = np.hstack((np.random.randn(nbase*4)*1.2+2.,np.random.randn(nbase*4)*2.8+1.0))

# uncomment below for displaying the histogram plots
plt.hist(vs, bins=50, color='y', range=(-5.,7.), alpha=0.5)
plt.hist(vb, bins=50, color='g', range=(-5.,7.), alpha=0.5)
plt.show()

def find_the_best_window():
    output = np.zeros(2)
    ### START YOUR CODE HERE ###
    
    def Z_func(l_u_array):
        L = l_u_array[0]
        U = l_u_array[1]
        ns = 0
        nb = 0
        for i in range(len(vs)):
            if vs[i] > L:
                if vs[i] < U:
                    ns += 1
            
        for i in range(len(vb)):
            if vb[i] > L:
                if vb[i] < U:
                    nb += 1
                    
        z = (ns+nb)**0.5/ns
        return z
    
    init = np.array([2,4])
    r = opt.minimize(Z_func, init, method='Nelder-Mead')
    if r.success:
        output[0], output[1] = round(r.x[0], 2),round(r.x[1], 2)+0.01
    #### END YOUR CODE HERE ####
    return output
print(find_the_best_window())