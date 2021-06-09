#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:18:38 2020

@author: petcheme
"""


import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from mpl_toolkits.mplot3d import Axes3D
import numpy as np


""" parametros """

# frecuencias
k = 2*np.pi       # \_ elijo valores cómodos
w = 2*np.pi       # /
c = w / k

# amplitudes (reales) y desfasajes para cada oscilación transversal
A_h   = 1
A_v   = 1
phi_h = 0
phi_v = 1

# flag para el caso de la cuerda rotante
cuerda_rotante = False

# coordenadas a evaluar
t = np.linspace(start=0, stop=5, num=150)
x = np.linspace(start=0, stop=5, num=1000)       # llamo x a la direccion de propagacion


""" evaluacion """

# voy a aprovechar la operatoria matricial al máximo, voy a obtener todos mis
# datos sin hacer un solo loop ;)

# el primer paso es armar un mesh para ambas coordenadas
t_grilla, x_grilla = np.meshgrid(t, x)

# el siguiente paso es evaluar la función en ambos mesh's, para obtener el campo
# en mis direcciones ortogonales:
campo_h = A_h*np.exp(1j*(k*x_grilla - w*t_grilla + phi_h))
campo_v = A_v*np.exp(1j*(k*x_grilla - w*t_grilla + phi_v))
               
               
if cuerda_rotante:
    # sumo onda viajera regresiva para obtener onda estacionaria
    campo_h += A_h*np.exp(1j*(k*x_grilla + w*t_grilla - phi_h))
    campo_v += A_v*np.exp(1j*(k*x_grilla + w*t_grilla - phi_v))
    
    # multiplico por la unidad imaginaria para obtener un seno en la posicion
    campo_h *= 1j
    campo_v *= 1j


""" graficar """

# parametros para proyectar el campo
z_proj =  3
y_proj = -3
    
# defino mi figura y ejes
fig    = plt.figure()
ax     = fig.add_subplot(111, projection = "3d")

# defino mis lineas, luego modifico sus coordenadas para realizar la animacion

# campo en 3D
lin3d, = ax.plot(x, np.real(campo_h[:,0]),
                    np.real(campo_v[:,0]))

# campo para posicion = 0
lin_x, = ax.plot(x_grilla[0,], np.real(campo_h[0,]), np.real(campo_v[0,]))

# componentes H y V
lin_h, = ax.plot(x, np.real(campo_h[:,0]), y_proj)
lin_v, = ax.plot(x, z_proj*np.ones(x.shape), np.real(campo_v[:,0]))

# vector E
lin_E, = ax.plot((0,0),
                 (0,np.real(campo_h[0,0])),
                 (0,np.real(campo_v[0,0])))

# ejes de referencia:
# ax.plot((0,5), (0,0), (0,0), color='gray')              # de propagacion
# ax.plot((0,5), (3,3), (0,0), color='gray')              # para la componente vertical
# ax.plot((0,5), (0,0), (-3,-3), color='gray')            # para la componente horizontal

ax.set_xlabel('z')
ax.set_ylabel('H')
ax.set_zlabel('V')

ax.set_xlim((x[0],x[-1]))
ax.set_ylim((-3,3))
ax.set_zlim((-3,3))

# ticks de los ejes
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.zaxis.set_major_locator(ticker.MultipleLocator(1))

def animacion(frame):
    
    plt.title('t={:.1f}, '.format(t[frame]) +
              'frame={:.0f}'.format(frame))
                 
    # update 3d line
    lin3d.set_data(x,       np.real(campo_h[:,frame]))
    lin3d.set_3d_properties(np.real(campo_v[:,frame]))
     
    # update zero-position projection
    #lin_x.set_data(x[0],    np.real(campo_h[0,0:frame+1]))
    #lin_x.set_3d_properties(np.real(campo_v[0,0:frame+1]))
    
    # update H projection
    lin_h.set_data(x, np.real(campo_h[:,frame]))
    lin_h.set_3d_properties(y_proj)

    # update V projection
    lin_v.set_data(x, z_proj*np.ones(x.shape))
    lin_v.set_3d_properties(np.real(campo_v[:,frame]))

    # E vector
    my_pos = x[0]
    idx = (np.abs(x - my_pos)).argmin()
    lin_E.set_data((x[idx], x[idx]),
                            (0, np.real(campo_h[idx,frame])))
    lin_E.set_3d_properties((0, np.real(campo_v[idx,frame])))
    

    return 

ani = animation.FuncAnimation(fig, animacion, frames=np.arange(0, t.size),
                              interval=80, repeat=False)


