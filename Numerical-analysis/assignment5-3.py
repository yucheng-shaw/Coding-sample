#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:05:41 2018

@author: gener
"""

import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    q, m = 1., 1.,
    dydt = np.zeros(6)
    ### START YOUR CODE HERE ###

    vx,vy,vz = y[3],y[4],y[5]
    dydt[0], dydt[1], dydt[2] = vx, vy, vz
    ax = q*Ex/m + q*(vy*Bz - vz*By)/m
    ay = q*Ey/m + q*(vz*Bx - vx*Bz)/m
    az = q*Ez/m + q*(vx*By - vy*Bx)/m
    dydt[3], dydt[4], dydt[5] = ax, ay, az

    #### END YOUR CODE HERE ####
    return dydt

def find_tracking_records(B, E):
    global Bx
    Bx = B[0]
    global By 
    By = B[1]
    global Bz
    Bz = B[2]
    global Ex
    Ex = E[0]
    global Ey
    Ey = E[1]
    global Ez
    Ez = E[2]
    positions = np.zeros((10,3))
    ### START YOUR CODE HERE ###
    
    t = 0
    #times = 0
    y = np.zeros(6)
    for i in range(10):
        sol = solve_ivp(f, [t, t+1.], y) 
        y = sol.y[:,-1]
        t = sol.t[-1]
        #times += 0.1
        #print("%.2f" % t)
        #print(("%.1f" % t) == any([1.0,2.0,3,4,5,6,7,8,9,10]))
        #for i in range(10):
            #print('hii')
        positions[i] = [y[0], y[1], y[2]]
        #if t % 1 < 1E-9:
            #positions[t] = [y[0], y[1], y[2]]
            
    #### END YOUR CODE HERE ####
    return positions
print(find_tracking_records([1,2,3],[1,1,1]))