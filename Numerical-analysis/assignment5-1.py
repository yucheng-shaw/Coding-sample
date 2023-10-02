#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 20:05:36 2018

@author: gener
"""

import numpy as np
from scipy.integrate import solve_ivp

def f(t,y,k):
    m, g = 1., 9.8
    dydt = np.zeros(4)
    ### START YOUR CODE HERE ###
    
    vx = y[2]
    vy = y[3]
    v = (vx**2+vy**2)**0.5
    ax = -k*v**2*vx/(m*v)
    ay = -k*v**2*vy/(m*v)-g
    dydt[0],dydt[1],dydt[2],dydt[3] = vx, vy, ax, ay

    #### END YOUR CODE HERE ####
    return dydt

def flight_distance(theta, v0, k):
    distance = 0.
    ### START YOUR CODE HERE ###
    
    t = 0
    y = [0,0,v0*np.cos(theta),v0*np.sin(theta)]
    h = 0.001
    
    while y[1] >= 0:
        k1 = f(t,y,k)
        k2 = f(t+0.5*h, y+0.5*h*k1,k)
        k3 = f(t+0.5*h, y+0.5*h*k2,k)
        k4 = f(t+h, y+h*k3,k)
        y += h/6.*(k1+2.*k2+2.*k3+k4)
        t += h
       
    distance = y[0]
    
    #### END YOUR CODE HERE ####
    return distance

print(flight_distance(np.pi/4, 10, 0.1))