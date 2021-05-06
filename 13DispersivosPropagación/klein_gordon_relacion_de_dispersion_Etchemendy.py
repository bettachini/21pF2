#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:36:07 2020

@author: petcheme
"""
import numpy as np
import matplotlib.pyplot as plt

# relación de dispersión de klein-gordon

omega_0_values = [0,1,2]
c_sq = 1

fig, ax = plt.subplots(nrows=2)

k_values = np.linspace(0, 4, num=500)

for omega_0 in omega_0_values:

    omega    = np.sqrt(omega_0**2 + c_sq*k_values**2 )
    derivada = c_sq *k_values / omega
    ax[0].plot(k_values, omega,    label = 'omega_0='+'{:.0f}'.format(omega_0))
    ax[1].plot(k_values, derivada, label = omega_0)
    
# ax.fill_between(delta_k, 0.5/delta_k, 0.5/delta_k[1], alpha=0.1)
# ax.plot(delta_k, 0.5/delta_k, linestyle='--')

vf = omega / k_values
    
ax[1].set_xlabel('$k$')
ax[0].set_ylabel('$\omega(k)$')
ax[1].set_ylabel('$d\omega / dk$')
ax[0].set_title('Ec. de Klein-Gordon con $c^2$ = {:.0f}'.format(c_sq))

ax[0].legend()