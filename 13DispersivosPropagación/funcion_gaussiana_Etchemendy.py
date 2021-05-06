#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:31:56 2020

@author: petcheme
"""
import numpy as np
import matplotlib.pyplot as plt

# defino la expresión de la gaussiana en una función
def mi_gaussiana(x, x0, delta):
    return np.exp(-((x-x0) / 2 / delta)**2)

# parametros
k0      = 50        # posición del pico de la campana
delta_k = 3         # ancho de la campana
A       = 2
k_valores = np.linspace(start=40, stop=60, num=1000)

# notar que la amplitud está por fuera de la definición de la función
F_k = A*mi_gaussiana(k_valores, k0, delta_k)

# creo handles para la figura y los ejes
fig = plt.figure()
ax  = plt.axes()

# grafico la gaussiana
ax.plot(k_valores, F_k, label='F(k)')
ax.set_xlabel('k')
ax.set_ylabel('F(k)')
ax.title

# indico el centro de la campana
ax.axvline(k0, linestyle='--')

# indico el ancho de la campana
k_ancho = np.array([k0 - delta_k, k0 + delta_k])
F_ancho = A*mi_gaussiana(k_ancho, k0, delta_k)

head_length = delta_k/5
ax.arrow(k0, F_ancho[0],   delta_k-head_length,  0, head_length=head_length, head_width=.05, color='orange')
ax.arrow(k0, F_ancho[0], -(delta_k-head_length), 0, head_length=head_length, head_width=.05, color='orange')

# anotaciones
ax.annotate('$\Delta k$',
            xy=(k0-delta_k/2, 1.01*A*mi_gaussiana(k0+delta_k, k0, delta_k)),
            color='orange')
ax.annotate('$F(k_0)$',
            xy=(k0+2*delta_k, A*mi_gaussiana(k0, k0, delta_k)))
ax.annotate('$F(k_0 \pm \Delta k)$',
            xy=(k0+2*delta_k, A*mi_gaussiana(k0+delta_k, k0, delta_k)))


ax.axvspan(k0-delta_k, k0+delta_k, alpha=0.1)
ax.axhspan(F_ancho[0], A, alpha=0.1)


# lo que sigue es opcional:

# Tambien podemos usar la gaussiana del paquete de estadistica de scipy
# from scipy.stats import norm

# Hay que tener en cuenta que en estadistica la funcion se define de modo que:
# - el área bajo la curva debe ser uno
# - el ancho de la curva se define mediante la desviación estándar
#
# Esto significa que debemos definir un coeficiente para "renormalizar" la
# amplitud, y debemos transformar el ancho delta_k en una desviación estándar,
# para esto usamos un factor sqrt(2) multiplicando a delta_k
#
# Ver: https://en.wikipedia.org/wiki/Normal_distribution

# sigma = delta_k*np.sqrt(2)                          # sigma es el desvio estándar
# factor_normalizacion = 1/sigma / np.sqrt(2*np.pi)   # notar que se usa el desvío estandar en el factor de normalizacion

# F_k2 = A/factor_normalizacion *norm.pdf(k_valores, k0, sigma)

# ax.plot(k_valores, F_k2, label='F(k) 2')
# ax.legend()
