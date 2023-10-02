#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:05:41 2018

@author: gener
"""
import time
import numpy as np
from scipy.integrate import solve_ivp

init_data = [[0.362, +0.380, -1.954, -2.364, +0.461],
             [0.168, +0.032, +0.631, +0.233, -0.608],
             [0.413, +0.280, -0.095, -0.672, -0.369],
             [0.209, -1.669, +0.116, -1.965, +0.237],
             [0.172, +0.376, +0.673, -0.370, +0.723],
             [0.322, -0.583, +0.355, -0.405, +0.831],
             [0.289, -0.619, -0.960, -0.525, -1.366],
             [0.108, +0.626, -1.931, +0.276, +1.698],
             [0.491, +0.499, +0.217, -1.237, +0.084],
             [0.325, +0.781, +1.452, -0.295, -0.827]];

def f(t,y):
    dydt = np.zeros(40)
    ### START YOUR CODE HERE ###
    
    init_data_np = np.array(init_data)
    mass = init_data_np[:, 0]
    y_reshape = y.reshape(10,4)
    #print(y_reshape)
    #time.sleep(1)
    for i in range(10):
        x,y_pos,vx,vy = y_reshape[i][0],y_reshape[i][1],y_reshape[i][2],y_reshape[i][3]
        ax, ay = 0, 0
        for j in range(10):
            if i != j:
                ax += mass[j]*(y_reshape[j][0]-x)/((x-y_reshape[j][0])**2+(y_pos-y_reshape[j][1])**2)**(3/2)
                ay += mass[j]*(y_reshape[j][1]-y_pos)/((x-y_reshape[j][0])**2+(y_pos-y_reshape[j][1])**2)**(3/2)
            
        y_reshape[i][0], y_reshape[i][1], y_reshape[i][2], y_reshape[i][3] = vx, vy, ax, ay
        
    dydt = y_reshape.reshape(40)

    #### END YOUR CODE HERE ####
    return dydt

def solve_for_gravity(delta_t):
    positions = np.zeros((10,2))
    ### START YOUR CODE HERE ###
    
    t = 0
    init_data_np = np.array(init_data)
    y0 = init_data_np[:, 1:]
    y = y0.reshape(40)
    while t < delta_t:
        #y = y0.reshape(40)
        sol = solve_ivp(f, [t, t+0.1], y) 
        y = sol.y[:,-1]
        t = sol.t[-1]
        #print(t)
        
    all = y.reshape(10,4)
    positions = all[:, :2] 
    
    #### END YOUR CODE HERE ####
    return positions
print(solve_for_gravity(0.01))