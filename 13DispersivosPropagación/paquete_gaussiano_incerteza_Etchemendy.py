#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:49:29 2020

@author: petcheme
"""
import numpy as np
import matplotlib.pyplot as plt

# valores para el coeficiente del término de fase cuadrático
beta_valores = [10, 20, 50]

# valores de delta k, uso un espaciado logarítmico para samplear cerca del cero
# con buena precisión sin aumentar la cantidad de valores lejos del 0
delta_k = np.logspace(-2.4, 0, num=1000)

# preparo la figura
fig, ax = plt.subplots()

# recorro los valores de beta y muestro la relación de incerteza en cada caso
for beta in beta_valores:

    delta_x = 0.5*np.sqrt(1 + 16* beta**2 * delta_k**4) / delta_k
    ax.plot(delta_k, delta_x, label='beta='+'{:.0f}'.format(beta))
    
ax.fill_between(delta_k, 0.5/delta_k, 0.5/delta_k[0], alpha=0.1)
ax.plot(delta_k, 0.5/delta_k, linestyle='--', color='cornflowerblue', label='$\Delta x \Delta k = 1/2$')

    
ax.set_xlabel('$\Delta k$')
ax.set_ylabel('$\Delta x$')
ax.set_title('Relación de incerteza para gaussiana con fase cuadrática')
ax.legend(loc='best')