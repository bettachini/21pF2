#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:44:20 2020

@author: petcheme
"""

import numpy as np
import matplotlib.pyplot as plt


theta_0 = 0.4
angulos = np.linspace(0, np.pi*2, num=200)

fig, ax = plt.subplots()

ax.plot(angulos, np.cos(angulos - theta_0) **2)

idx = np.arange(200, step=9)
ax.scatter(angulos[idx], np.cos(angulos[idx] - theta_0) **2 +
           np.random.normal(scale=.03, size=23))


ax.set_xlabel('\\theta')
ax.set_ylabel('I_salida / I_fuente')

