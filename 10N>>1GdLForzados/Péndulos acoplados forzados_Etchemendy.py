# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:58:27 2021

@author: petcheme
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import numpy.matlib as npm

# pendulos acoplados

# setear el caso
# luego elegir la frecuencia dentro del bloque de parametros de cada caso
que_caso = 1

# caso 1

if que_caso == 1:       # sistema de 10 péndulos acoplados

    m = 2.
    k = 10.
    g = 10.
    
    N = 10
    N2 = 0
    N3 = 0
    
    l1 = 1.
    l2 = 0.8
    l3 = 1.
    
    # seleccionar una y comentar las demás:
    w_ext = 1e-5        # frecuencia baja con k más grande posible
                        # al aumentar la frecuencia, la atenuación ocurre en mayor distancia
#    w_ext = 3.1622         # limite inferior antes del primer modo
                        # probar con valores cada vez más cercanos a 3.16227766016838

#    # REFERENCIA: frecuencias de los modos para este sistema
#    # array([ 3.16227766,  3.2387397 ,  3.45106216,  3.75794458,  4.11215638,
#    #         4.47213595,  4.80522319,  5.08702787,  5.30001603,  5.43236276])

#    w_ext = 3.10      # frecuencia intermedia entre modos 1 y 2
#    w_ext = 3.2387396988718415  # comparar con frec del modo 2
    
#    w_ext = 10.5         # modos exponenciales superiores
                        # al aumentar la frecuencia, la atenuación ocurre en menor distancia

elif que_caso == 2:     # dos sistemas compatibles de 50 péndulos acoplados con diferente largo

# frecuencias para péndulos largos
#array([ 3.16227766,  3.16352542,  3.16726083,  3.17346041,  3.18208538,
#        3.1930822 ,  3.20638333,  3.2219081 ,  3.23956375,  3.25924658,
#        3.28084319,  3.30423169,  3.32928303,  3.35586227,  3.38382979,
#        3.41304248,  3.44335488,  3.47462017,  3.50669115,  3.53942111,
#        3.57266455,  3.60627792,  3.64012015,  3.67405322,  3.70794255,
#        3.74165739,  3.77507114,  3.80806157,  3.84051107,  3.87230675,
#        3.90334062,  3.93350966,  3.96271588,  3.99086641,  4.01787346,
#        4.04365441,  4.06813175,  4.09123312,  4.11289126,  4.13304403,
#        4.15163437,  4.16861028,  4.1839248 ,  4.19753597,  4.20940684,
#        4.21950543,  4.22780471,  4.23428258,  4.23892189,  4.24171038])

# frecuencias para péndulos cortos
#array([ 3.33333333,  3.33451709,  3.33806116,  3.34394409,  3.35213044,
#        3.3625712 ,  3.37520446,  3.38995618,  3.40674102,  3.42546339,
#        3.44601845,  3.46829326,  3.49216789,  3.51751655,  3.54420868,
#        3.57211003,  3.60108372,  3.63099111,  3.66169277,  3.69304927,
#        3.7249219 ,  3.75717335,  3.7896683 ,  3.82227395,  3.85486044,
#        3.88730126,  3.91947359,  3.95125854,  3.98254145,  4.01321201,
#        4.04316449,  4.07229779,  4.10051561,  4.12772647,  4.1538438 ,
#        4.17878596,  4.2024763 ,  4.22484314,  4.24581978,  4.26534454,
#        4.28336072,  4.2998166 ,  4.31466544,  4.32786545,  4.3393798 ,
#        4.34917661,  4.35722891,  4.36351465,  4.3680167 ,  4.37072283])

    m = 1.
    k = 2.
    g = 10.
    
    N = 100
    N2 = 50
    N3 = 0
    
    l1 = 1
    l2 = 0.9
    l3 = 1.
    
    w_ext = 3.16227766    # modo fundamental para pendulos largos
#    w_ext = 3.33333333    # modo fundamental para pendulos cortos
#    w_ext = 3.7           # frecuencia intermedia
#    w_ext = 4.24171038    # modo superior para pendulos largos
#    w_ext = 4.37072283    # modo superior para pendulos cortos
    
elif que_caso == 3:   # dos sistemas incompatibles de 50 péndulos acoplados con diferente largo

# frecuencias para péndulos largos
#array([ 3.16227766,  3.16352542,  3.16726083,  3.17346041,  3.18208538,
#        3.1930822 ,  3.20638333,  3.2219081 ,  3.23956375,  3.25924658,
#        3.28084319,  3.30423169,  3.32928303,  3.35586227,  3.38382979,
#        3.41304248,  3.44335488,  3.47462017,  3.50669115,  3.53942111,
#        3.57266455,  3.60627792,  3.64012015,  3.67405322,  3.70794255,
#        3.74165739,  3.77507114,  3.80806157,  3.84051107,  3.87230675,
#        3.90334062,  3.93350966,  3.96271588,  3.99086641,  4.01787346,
#        4.04365441,  4.06813175,  4.09123312,  4.11289126,  4.13304403,
#        4.15163437,  4.16861028,  4.1839248 ,  4.19753597,  4.20940684,
#        4.21950543,  4.22780471,  4.23428258,  4.23892189,  4.24171038])

# frecuencias para pendulos cortos: NO COINCIDEN CON LOS LARGOS
#array([ 4.47213595,  4.47301834,  4.47566098,  4.48005033,  4.48616399,
#        4.49397084,  4.50343136,  4.51449796,  4.52711534,  4.54122101,
#        4.55674577,  4.57361422,  4.59174536,  4.6110532 ,  4.63144729,
#        4.65283344,  4.6751142 ,  4.69818958,  4.72195752,  4.74631455,
#        4.77115626,  4.79637785,  4.82187461,  4.84754237,  4.87327794,
#        4.89897949,  4.92454689,  4.94988211,  4.97488947,  4.99947593,
#        5.02355133,  5.04702865,  5.06982418,  5.09185769,  5.11305263,
#        5.13333625,  5.15263971,  5.17089822,  5.18805113,  5.20404198,
#        5.21881864,  5.23233329,  5.24454257,  5.25540752,  5.26489373,
#        5.27297127,  5.27961482,  5.28480359,  5.28852142,  5.29075674])

    m = 1.
    k = 2.
    g = 10.
    
    N = 100
    N2 = 50
    N3 = 0
    
    l1 = 1.
    l2 = 0.5
    l3 = 1.
    
    w_ext = 3.16227766    # modo fundamental para pendulos largos
#    w_ext = 4.24171038    # modo superior para pendulos largos
#    w_ext = 4.355
#    w_ext = 4.47213595    # modo fundamental para pendulos cortos
#    w_ext = 5.29075674    # modo superior para pendulos cortos
 

elif que_caso == 4:   # dos sistemas idénticos de 50 péndulos acoplados conectados mediante una región incompatible

    m = 1.
    k = 2.
    g = 10.
    
    N = 104
    N2 = 4
    N3 = 50
    
    l1 = 1.
    l2 = 0.8
    l3 = 1.
    
    w_ext = 4.2417    # modo fundamental para pendulos largos
#    w_ext = 3.96
#    w_ext = 4.24171038    # modo superior para pendulos largos
#    w_ext = 4.355
#    w_ext = 4.47213595    # modo fundamental para pendulos cortos
#    w_ext = 5.29075674    # modo superior para pendulos cortos   
#    w_ext = 4

elif que_caso == 5:
    m = 1.
    k = 2.
    g = 10.
    
    N = 10
    N2 = 0
    N3 = 0
    
    l1 = 1.
    l2 = .1
    l3 = .1
    
    w_ext = 4.2417    # modo fundamental para pendulos largos
    

# parametros del forzado
F_ext = np.array(np.zeros(N), ndmin=2).T
F_ext[0] = 1

# ¿que cambia si forzamos desde el otro extremo?
#F_ext[-1] = 1

# eje del tiempo
t = np.linspace(0, 2*np.pi/w_ext*5, 200)


# ---- a continuacion armo las matrices ----

m_vector = m*np.ones(N)              # vector de masas

# pendulos
parte1 = np.diag(np.concatenate(( np.ones(N-N2-N3), np.zeros(N2), np.zeros(N3)) ))
parte2 = np.diag(np.concatenate((np.zeros(N-N2-N3),  np.ones(N2), np.zeros(N3)) ))
parte3 = np.diag(np.concatenate((np.zeros(N-N2-N3), np.zeros(N2),  np.ones(N3)) ))


K_pendulos1 = np.matmul(-m*g/l1*np.diag(np.ones(N)), parte1)
K_pendulos2 = np.matmul(-m*g/l2*np.diag(np.ones(N)), parte2)
K_pendulos3 = np.matmul(-m*g/l3*np.diag(np.ones(N)), parte3)

K_pendulos = K_pendulos1 + K_pendulos2 + K_pendulos3

# acoplamiento
K_resortes  = -2*k*np.diag(np.ones(N)) + k*np.diag(np.ones(N-1),1) + k*np.diag(np.ones(N-1),-1)
K_resortes[0,0]     = -k        # \_ extremos libres
K_resortes[N-1,N-1] = -k        # /

# junto todo
K = K_pendulos + K_resortes

# disipacion
# incluyo una disipación despreciable en el sistema, para evitar
# divisiones por cero en las amplitudes forzadas
gamma = 1e-3 # chequear que este valor es verdaderamente despreciable para la configuración del sistema

# ---- parametros derivados ----

# Cantidad de masas
n_masas   = np.size(m_vector)
# Cantidad de samples para el gráfico
n_samples = t.size

# ---- Solucion de modos normales ----
M     = np.diag(m_vector)
M_inv = np.linalg.inv(M)
W     = np.dot(M_inv, K)
l, A  = np.linalg.eig(W)

w = np.sqrt(-l)

# No siempre las frecuencias quedan ordenadas de menor a mayor, uso argsort para 
# reordenar todo
indices_ordenados = np.argsort(w)
l = l[indices_ordenados]
w = w[indices_ordenados]
A = A[:,indices_ordenados]

# ---- Condiciones iniciales ----

# Como estoy interesado en el estacionario, no necesito plantear condiciones
# iniciales ;)

A_inv = np.linalg.inv(A)



# ---- Solución del forzado ----

# redefino el forzado usando los modos normales
# modo = 10
# F_ext = np.array(A[:,modo-1], ndmin=2).T
#w_ext = w[modo-1]

# Obtengo el vector de aceleraciones producidas por la fuerza externa
a_ext = np.dot(M_inv, F_ext)

# Transformo el vector de aceleraciones a la base de modos normales
a_ext_modos = np.dot(A_inv, a_ext)


# Obtengo las amplitudes para la solucion de modos normales forzados

# primero armo un vector que contiene los coeficientes de frecuencias
# y disipacion de las amplitudes forzadas
Afase = (w**2 - w_ext**2) / ((w**2 - w_ext**2)**2 + (gamma*w_ext)**2)
Acuad = w_ext*gamma / ((w**2 - w_ext**2)**2 + (gamma*w_ext)**2)

# los meto en una matriz y la aplico a las aceleraciones externas aplicadas sobre los modos
b_modos_fase = np.dot(np.diag(Afase), a_ext_modos)
b_modos_cuad = np.dot(np.diag(Acuad), a_ext_modos)

# Transformo a las amplitudes de las masas
b_masas_fase = np.dot(A, b_modos_fase)
b_masas_cuad = np.dot(A, b_modos_cuad)


# La solución estacionaria se escribe en una sola linea para la posicion y
# otra para la velocidad
psi_forzado = npm.repmat(b_masas_fase, 1,n_samples)*npm.repmat(np.cos(w_ext *t), n_masas, 1) + \
              npm.repmat(b_masas_cuad, 1,n_samples)*npm.repmat(np.sin(w_ext *t), n_masas, 1)

eje_masas =  np.array(range(N)) + 1

# ploteo las matrices del sistema
if (False):
    plt.figure(figsize=(14, 3.5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(M, cmap='RdBu', interpolation='none')
    plt.colorbar()
    plt.clim(-1, 1)
    
    plt.subplot(1, 3, 2)
    plt.imshow(-K, cmap='RdBu', interpolation='none')
    plt.colorbar(extend='both')
    plt.clim(-np.max(np.abs(K)), np.max(np.abs(K)))
    
    plt.subplot(1, 3, 3)
    plt.imshow(np.matmul(A_inv, np.matmul(W, A)), cmap='RdBu', interpolation='none')
    plt.colorbar(extend='both')
    plt.clim(-w[-1]**2, w[-1]**2)



# ploteo las amplitudes del forzante en funcion de la frecuencia
if (False):
    fig1, ax1 = plt.subplots()
    nro_modo = np.array(range(N))+1
    ax1.scatter(nro_modo, w)
    ax1.plot(nro_modo, np.sqrt(g/l1 + 4*k/m*np.sin( (nro_modo-1)*np.pi/2/N )**2))
    
    fig2, ax2 = plt.subplots()
    
    omega_ext = np.linspace(0.99*min(w), max(w)*1.01, num=20000)
    Aelas = np.zeros((N, omega_ext.size))
    Aabs  = np.zeros((N, omega_ext.size))
    for i in range(N):
        aux = (w[i]**2 - omega_ext**2)**2 + (gamma*omega_ext)**2
        Aelas[i,] = (w[i]**2 -omega_ext**2) / aux
        Aabs[i,]  = gamma*omega_ext / aux
        #ax2.plot(omega_ext, Aelas[i,], color='blue')
        ax2.plot(omega_ext, Aabs[i,], color='blue')
        ax2.set_xlim([3.1,4.3])
        #ax2.set_ylim([-170,170])
        ax2.set_ylim([-20,330])


# ploteo la animacion del sistema
fig, ax = plt.subplots()
line_plot, = ax.plot(eje_masas, 0*eje_masas)
scat_plot  = ax.scatter(eje_masas, 0*eje_masas) 

limite_y = np.max(psi_forzado)*1.1
limite_y = limite_y / 1
ax.set_ylim([-limite_y, limite_y])

def update_plot(que_frame):

    y = psi_forzado[:,que_frame]
    line_plot.set_ydata(y)

    scat_plot.set_offsets(np.array([eje_masas, y]).T)

    ax.set_title('frame={:.0f}'.format(que_frame))
   

ani = animation.FuncAnimation(fig, update_plot, frames=range(n_samples),
                              interval=100, repeat=False)

plt.show()




