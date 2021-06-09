#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:12:33 2020

@author: petcheme
"""

import numpy as np
import matplotlib.pyplot as plt

# para usar latex
from matplotlib import rc
#rc('font', **{'family':'serif','serif':['Palatino']})
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

Sa = 2
Sb = 1
J0 = np.array(((Sa),(Sb*1j)), ndmin=2).T 

# J0 = np.array(((np.sqrt(2)),(np.sqrt(2)*np.exp(1j*0.8))), ndmin=2).T 

x=.3
rot = np.array( ((np.cos(x), -np.sin(x)),
                 (np.sin(x),  np.cos(x))) )

A = np.matmul(rot, J0)

Ax = A[0]
Ay = A[1]
epsilon = np.angle(A[0])-np.angle(A[1])
alpha   = 0.5*np.arctan(2*np.abs(Ax)*np.abs(Ay)*np.cos(epsilon) / (np.abs(Ax)**2 - np.abs(Ay)**2))

# signo negativo para reflejar paso del tiempo cuando la propagacion es k*z - omega*t
fases = -np.linspace(0, 2*np.pi, 200)

fig, ax = plt.subplots()

# caja de la elipse
square_x = np.abs(Ax)*np.array((-1,1,1,-1,-1))
square_y = np.abs(Ay)*np.array((-1,-1,1,1,-1))
ax.plot(square_x, square_y, color='lightgray')

# semiejes
ax.plot((-Sa*np.cos(alpha), Sa*np.cos(alpha)), (-Sa*np.sin(alpha), Sa*np.sin(alpha)), color='mediumseagreen', linestyle='--')
ax.plot((-Sb*np.sin(alpha), Sb*np.sin(alpha)), (Sb*np.cos(alpha), -Sb*np.cos(alpha)), color='mediumseagreen', linestyle='--')
         
# amplitudes en x e y
ax.plot((0,np.abs(Ax)), (-np.abs(Ay)-.1,-np.abs(Ay)-.1), color='red')
ax.plot((-np.abs(Ax)-.1,-np.abs(Ax)-.1), (0,np.abs(Ay)), color='red')

pos=0.5
ax.annotate('$|A_x|$',(pos+.2,-np.abs(Ay)-.4), fontsize=20, color='red')
ax.annotate('$|A_y|$',(-np.abs(Ax)-.5,pos+.1), fontsize=18, color='red')

# ejes de coordenadas
dx=0.6
ax.arrow(0,0,dx=dx,dy=0, head_width=.1, head_length=.1)
ax.arrow(0,0,dx=0,dy=dx, head_width=.1, head_length=.1)

pos=0.7
ax.annotate('$E_x$',(pos,0), fontsize=18)
ax.annotate('$E_y$',(0,pos), fontsize=18)

# elipse
ax.plot(np.real(Ax*np.exp(1j*fases)),
        np.real(Ay*np.exp(1j*fases)))

# angulo
angulos = np.linspace(0,alpha,num=100)
rr=0.5
ax.plot(rr*np.cos(angulos), rr*np.sin(angulos),color='royalblue')

# la r antes del string es para usar latex
ax.annotate(r'$\alpha$',(rr*np.cos(angulos[-1])-.05,
                         rr*np.sin(angulos[-1])+.05), fontsize=20, color='royalblue')

# misc
ax.set_xlim((-3,3))
ax.set_ylim((-2,2))
ax.axis('off')
