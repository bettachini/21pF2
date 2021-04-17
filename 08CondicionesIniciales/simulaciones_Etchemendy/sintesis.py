#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:15:48 2020

@author: petcheme
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write


""" 1. parametros de entrada """

plot_modos = True

# parámetros del ejercicio 22, guía 1:

# características del sistema
L = .6                   # longitud del sistema
c = 340                 # velocidad de propagación 

gamma = 2               # disipacion


# condición inicial
psi_0 = .8              # amplitud inicial
alpha = .4             # posición del escalón, va entre 0 y 1

# exactitud de la solución
n_modos = 3000          # cuantos modos quiero sumar

duracion      = 4       # tiempo en segundos
sample_rate_t = 44100   # frecuencia de sampleo temporal

pos_x = 1*L



""" 2. parametros derivados """
n_samples_t = int(np.ceil(duracion*sample_rate_t))


""" 3. solución """

# 3a. amplitudes de modos
modos  = np.arange(1,n_modos+1, step = 1)   # vector de modos
k_wave = (2*modos-1)*np.pi/2/L              # vector de numeros de onda
omega  = np.sqrt((c*k_wave)**2 - 0.25 * gamma**2)
frec   = omega / 2 /np.pi

# obtengo el vector de amplitudes A_m
amplitudes = 2*psi_0/L/k_wave*np.cos(k_wave*L*alpha)


# 3b. solución en función del tiempo

# parametros del fundamental
omega_fund   = omega[0]
frec_fund    = frec[0]
periodo_fund = 1 / frec_fund

# eje de tiempo
eje_tiempo = np.linspace(start=0, stop=duracion, num=n_samples_t)


# reservo espacio para la solución
solucion = np.zeros(n_samples_t)

# calculo cada modo normal y lo asigno a una fila del array solucion
for modo in modos:
    
    omega_modo = np.sqrt((c*k_wave[modo-1])**2 - gamma**2 / 4)
    solucion  += amplitudes[modo-1]* \
                 np.sin(k_wave[modo-1]*pos_x)* \
                 np.cos(omega_modo*eje_tiempo)
                         

# sumo todos los modos normales (sumo las columnas del array)
solucion = solucion*np.exp(-0.5*gamma*eje_tiempo)


# gráfico de la amplitud versus número de modo
fig, ax = plt.subplots()
ax.plot(eje_tiempo, solucion)
ax.set_xlabel('Tiempo')
ax.set_ylabel('Onda')

write("salida_alpha_" + str(alpha) + ".wav", 44100, solucion)