#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:21:35 2020

@author: petcheme
"""

from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

Ax=1
Ay=2

# cantidad de diferencias de fase
n = 9


fig, ax = plt.subplots(ncols=5, nrows=2)

osc = np.exp(-1j*np.linspace(0, np.pi*2, num=200))      # invierto el signo para que aumento de la fase sea avance del tiempo

for i in np.arange(n):

    phase_diff_fraction = i/(n-1)

    if (i < n/2):
        this_ax = ax[0][i]
    else:
        this_ax = ax[1][i-5+1]

    this_ax.set_title(str(2*Fraction(i,n-1))+str('$\pi$'))
    this_ax.axis('off')
    this_ax.plot((-Ax, Ax, Ax, -Ax, -Ax),
                (-Ay, -Ay, Ay, Ay, -Ay),color='lightgray')

    Ex = np.real(Ax*osc)
    Ey = np.real(Ay*osc*np.exp(2j*phase_diff_fraction*np.pi))
    this_ax.plot(Ex, Ey)
    
    if not((2*phase_diff_fraction % 1) < .05 or
           (2*phase_diff_fraction % 1) > .95):
        hl=0.15
        hw=0.15
        this_ax.arrow(Ex[0], Ey[0],
                      dx=Ex[1]-Ex[0],
                      dy=Ey[1]-Ey[0], head_width =hw,
                                      head_length=hl)

    if (i == 0):    
        hl=0.1
        hw=0.1
        this_ax.arrow(0, 0, dy=0, dx=0.5*Ax-hl, head_width=hw, head_length=hl)
        this_ax.arrow(0, 0, dx=0, dy=0.5*Ay-hl, head_width=hw, head_length=hl)
        this_ax.annotate('$E_x$',(0.5*Ax,0))
        this_ax.annotate('$E_y$',(0,0.5*Ay))
        
        ax[1][0].axis('off')        
    