#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:24:21 2020

@author: petcheme
"""

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation

""" funciones personalizadas """
def mi_gaussiana(x, x0, delta_x):
    return np.exp(-((x-x0) / 2 / delta_x)**2)

""" 1. parámetros de entrada """

# parámetros del paquete
k0      = 50
delta_k = 5
A       = 10
alfa    = 0     # pendiente para el desfasaje espectral, es el corrimiento espacial de la envolvente

# parámetros del medio
vf = 1.0      # \_ tomando valores iguales estoy asumiendo un medio con relación
vg = 1.0      # /  de dispersión lineal y homogénea

# valores de k, x y t para los gráficos
k_valores = np.linspace(start=0, stop=100, num=100) 

# defino a x y t tomando como referencia:
# x: el ancho de la envolvente gaussiana 
# t: el tiempo requerido para avanzar dicho ancho
t_valores = np.linspace(start=  0, stop=10, num=1000) 
x_valores = np.linspace(start=-10, stop=10, num=1000) 


""" 2. parámetros derivados """

# frecuencia angular y período asociados a la onda descrita por k0
omega0 = k0*vf
tau0   = 1 / omega0 / 2 / np.pi

# ancho de la envolvente gaussiana
delta_x = 1 / 2 / delta_k

# redefino los ejes x y t en función de estos parámetros derivados
t_valores = t_valores*delta_x / vg
x_valores = x_valores*delta_x

# la amplitud en el espacio x-t
Ax = 2*np.sqrt(np.pi)*A*delta_k


""" 3. Salida en pantalla """

# 1. muestro el espectro de amplitudes

F_k = A *mi_gaussiana(k_valores, k0, delta_k)

fig = plt.figure()
ax  = plt.axes()

ax.plot(k_valores, F_k, label='F(k)')
ax.axvline(k0)
ax.set_xlabel('k')
ax.set_ylabel('F(k)')
ax.set_title('Espectro de amplitudes para los números de onda')

# 2. muestro la envolvente, la portadora y la onda en el espacio, al principio y al final
fig2, ax2 = plt.subplots(nrows=3)

# cambiando los indices puedo elegir los momentos del tiempo que yo quiera
for t in t_valores[[0,-1]]:

    env  = mi_gaussiana(x_valores, vg*t - alfa,  1 / 2 / delta_k)   # uso amplitud 1
    port = np.cos(k0*(x_valores - vf*t))
    
    ax2[0].plot(x_valores, env, label='t=' + '{:2g}'.format(t))
    ax2[1].plot(x_valores, port)
    ax2[2].plot(x_valores, Ax*env*port)

    # agrego la envolvente
    ax2[2].plot(x_valores, Ax*env, linestyle='--', linewidth=1, color='grey')   # \_ para graficar la envolvente es necesario
    ax2[2].plot(x_valores,-Ax*env, linestyle='--', linewidth=1, color='grey')   # /  usar ambos signos

# etiquetas de ticks eje x, elimino las innecesarias
ax2[0].set_xticklabels([])
ax2[1].set_xticklabels([])

# etiquetas de ejes, leyendas y titulo
ax2[0].set_title('La envolvente, la portadora y la onda en el espacio')
ax2[0].set_ylabel('Envolvente')
ax2[1].set_ylabel('Portadora')
ax2[2].set_ylabel('Onda')
ax2[2].set_xlabel('x')
ax2[0].legend()

# 3. figura bidimensional

# el primer paso es armar una matriz con tantas filas y columnas como puntos
# en el tiempo y el espacio voy a considerar
onda_matriz = np.zeros((x_valores.size, t_valores.size))

# en este loop lleno de datos la matriz
c = 0
for t in t_valores:
    env  = mi_gaussiana(x_valores, vg*t - alfa,  1 / 2 / delta_k)   # uso amplitud 1
    port = np.cos(k0*(x_valores - vf*t))
    
    onda_matriz[:,c] = Ax*env*port

    c += 1

# preparo la figura
fig3, ax3 = plt.subplots()

img = ax3.imshow(onda_matriz,
                 cmap='Greens',                                                      # <- elijo el colormap
                 aspect = 'auto', origin='lower',                                    # <- relacion de aspecto y posición del origen
                 extent=[t_valores[0], t_valores[-1], x_valores[0], x_valores[-1]])  # <- ajusto los valores para los ejes

t1 = 0.5
x1 = vg*t1
ax3.axvline(t1, linestyle='--', color='lightyellow', linewidth=2)
ax3.axhline(x1, linestyle='--', color='lightyellow', linewidth=2)
    
# etiquetas de ejes y titulo
ax3.set_xlabel('t')
ax3.set_ylabel('x')
ax3.set_title('La función de onda en función de x y de t')

fig3.colorbar(img) # muestro el código de colores para la amplitud de la onda

# 4. muestro el paquete de onda en función del tiempo o de la posicion, según lo
# indicado en la figura 3
fig4, ax4 = plt.subplots(ncols=2)

# primer subplot, en función de t
env0  = mi_gaussiana(x1, vg*t_valores - alfa,  1 / 2 / delta_k)
port0 = np.cos(k0*(x1 - vf*t_valores))
ax4[0].plot(t_valores,  Ax*env0*port0)
ax4[0].plot(t_valores,  Ax*env0, linestyle='--', color='lightblue')    # \_ agrego la envolvente
ax4[0].plot(t_valores, -Ax*env0, linestyle='--', color='lightblue')    # /
    
ax4[0].set_xlabel('t')
ax4[0].set_ylabel('$\Psi$')
ax4[0].set_title('La función de onda en x fijo')

# segundo subplot, en función de x
env1  = mi_gaussiana(x_valores, vg*t1 - alfa,  1 / 2 / delta_k)
port1 = np.cos(k0*(x_valores - vf*t1))
ax4[1].plot(x_valores,  Ax*env1*port1)
ax4[1].plot(x_valores,  Ax*env1, linestyle='--', color='lightblue')
ax4[1].plot(x_valores, -Ax*env1, linestyle='--', color='lightblue')

ax4[1].set_xlabel('x')
# ax4[1].set_ylabel('$\Psi$')
ax4[1].set_title('La función de onda en t fijo')
