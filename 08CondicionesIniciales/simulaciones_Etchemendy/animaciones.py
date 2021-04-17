#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:15:48 2020

@author: petcheme
"""

import matplotlib.pyplot    as plt
import matplotlib.animation as animation
import numpy as np
import numpy.matlib


""" 1. parametros de entrada """

plot_modos = True

# parámetros del ejercicio 22, guía 1:

# características de la cuerda
L = 1                   # longitud de la cuerda
c = 1                   # velocidad de propagación de ondas en la cuerda

# condición inicial
psi_0 = 1               # amplitud inicial
alpha = .25             # posición del escalón, va entre 0 y 1

# exactitud de la solución
n_modos = 500          # cuantos modos quiero sumar

n_ciclos      = 1       # cuantos ciclos del fundamental dura la simulación
sample_rate_t = 500     # frecuencia de sampleo temporal

n_samples_x = 200       # cuantos puntos grafico en la coordenada x


limite_y = 1.2


""" 2. parametros derivados """
n_samples_t = int(np.ceil(n_ciclos*sample_rate_t))


""" 3. solución """

# 3a. amplitudes de modos
modos  = np.arange(1,n_modos+1, step = 1)   # vector de modos
k_wave = (2*modos-1)*np.pi/2/L              # vector de numeros de onda

# obtengo el vector de amplitudes A_m
amplitudes = -2*psi_0/L/k_wave*(np.cos(k_wave*L) - np.cos(k_wave*L*alpha))

# gráfico de la amplitud versus número de modo
fig_a = plt.figure()
ax_a = plt.axes()
max_modo = min(30, n_modos)
plt.bar(modos[0:max_modo], amplitudes[0:max_modo])
plt.xticks(np.linspace(1, max_modo, num=max_modo))
ax_a.set_xlabel('m')
ax_a.set_ylabel('A_m')


# 3b. solución en función del tiempo

# parametros del fundamental
omega_fund   = k_wave[0]*c
frec_fund    = omega_fund / 2 / np.pi
periodo_fund = 1 / frec_fund

# ejes de tiempo y de posición
eje_tiempo   = np.linspace(start=0, stop=n_ciclos*periodo_fund, num=n_samples_t)
eje_posicion = np.linspace(start=0, stop=L, num=n_samples_x)


# preparo el grafico para hacer la animacion
fig_psi   = plt.figure()
ax_psi    = plt.axes(xlim=(0,L),ylim=(-limite_y, limite_y))
line_psi, = ax_psi.plot(eje_posicion, 0*eje_posicion)

# ticks del eje x
# ax_psi.set_xticks(ticks=[-1,0,1,2])  
# ax_psi.set_xticklabels(labels=['-L','0','L','2L'])


ax_psi.set_xticks(ticks=[0,.25,.5,.75,1])  
ax_psi.set_xticklabels(labels=['0','L/4','L/2','3/4L','L'])

# etiquetas de ejes
ax_psi.set_xlabel('x')
ax_psi.set_ylabel('Psi')

# ploteo los modos para acompañar?
if plot_modos:
    lin_modos = np.matlib.repmat(line_psi,3,1)
    
    for i in np.arange(0,3):
        lin_modos[i], = ax_psi.plot(eje_posicion, 0*eje_posicion,lw=1)
    


def sol_temp(t):

    # reservo espacio para la solución en un instante del tiempo, armo un array con
    # n_modos filas y n_samples_x columnas
    solucion = np.zeros([n_modos, n_samples_x])
    
    # calculo cada modo normal en este instante, cada modo es asignado
    # a una fila del array solucion
    for modo in modos:
        solucion[modo-1,] = amplitudes[modo-1]* \
                            np.sin(k_wave[modo-1]*eje_posicion)* \
                            np.cos(c*k_wave[modo-1]*t)
                            
    # sumo todos los modos normales (sumo las columnas del array)
    sol_total = np.sum(solucion, axis=0)
    
    plt.title('t={:.2f}'.format(t))
    
    # agrego el grafico de los primeros 3 modos
    if plot_modos:
        for i in np.arange(0, 3):
            lin_modos[i,0].set_ydata(solucion[i,])
    
    
    line_psi.set_ydata(sol_total)

    return line_psi,

# sol_temp(eje_tiempo[0])

ani = animation.FuncAnimation(fig_psi, sol_temp, frames=eje_tiempo,
                              interval=100, repeat=False)

plt.show()

# ani.save('archivo.mp4')
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save(filename="movie.mp4", writer=writer)      

