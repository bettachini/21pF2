import matplotlib.pylab as plt
from matplotlib.widgets import Slider
import numpy as np
from matplotlib import animation

#Defino algunas funciones que voy a necesitar
def posicion(t,omega):
    '''
    Tanto t como omega pueden ser floats o arrays (no usar listas).
    Si ambos son floats devuelvo floats A,B y X que son las amplitudes para un dado omega y la posición para un omega para ese tiempo.
    Si t es array y omega es float devuelvo floats A y B que me definen donde estoy dentro de la curva de resonancia y X(t) que me muestra la evolucion temporal dentro de esa curva.
    Si t es float y omega es array devuelvo A(omega) y B(omega) que me definen toda la curva de resonancia y X(omega) para un tiempo fijo
    Si ambos son arrays me devuelve A(t*omega), B(t*omega) X(t*omega) que es equivalente a asignar en cada tiempo un omega distinto (barrido de frecuencias)
    '''
    m=1
    F = 1
    omega0 = 2
    gamma = 0.5

    A = (F/m)*gamma*omega/(gamma**2 * omega**2 + (omega0**2 - omega**2)**2)    
    B = (F/m)*(omega0**2 - omega**2)/(gamma**2 * omega**2 + (omega0**2 - omega**2)**2)
    X = A*np.sin(omega*t) + B*np.cos(omega*t)
    
    return [A,B,X]

def update(val):
    '''
    qué pasa cuando se actualiza algún slider
    '''
    t = sli_time.val    
    omega = sli_omega.val
    A,B,X = posicion(t,omega)

    lineA.set_data(omega,np.sqrt(A**2+B**2))
    lineRes.set_xdata([-2,X])
    lineM.set_xdata(X)
    lineX.set_ydata(posicion(tvar,omega)[2])

    fig.canvas.draw_idle()
    
    return (lineA,lineRes,lineM,lineX)
    
def auto_update(i):
    '''
    La animación está hecha sobre un slider tiempo, esta función actualiza el valor del slider tiempo a cada paso
    '''
    t = (sli_time.val + 0.4)
    sli_time.set_val(t)
    lineA,lineRes,lineM,lineX = update(t)
    return (lineA,lineRes,lineM,lineX)

#crear los ejes
fig,(axX,axM,axA) = plt.subplots(1,3)
fig.set_size_inches((10,3)) 
fig.tight_layout(pad=3.0) 
fig.subplots_adjust(bottom = 0.2,top = 0.75)

#Crear el axes para el slider
ax_sli_time = fig.add_axes([0.5,0.9,0.03, 0.00001])
ax_sli_omega = fig.add_axes([0.3,0.8,0.4,0.05])

#Convertir el axes en un slider
sli_time = Slider(ax=ax_sli_time,label='t', valmin = 0, valmax = 10, valfmt = '%1.1f s',valinit = 0, facecolor = 'blue')
sli_omega = Slider(ax=ax_sli_omega,label='$\Omega$ ', valmin = 0.5, valmax = 5, valinit = 2, valfmt = '%1.1f $s^{-1}$', facecolor = 'blue')

#Plotear data por default

axX.set_xlim((0,10)) 
axX.set_ylim((-1.5,1.5))
axX.grid()
axX.set_xlabel('Tiempo')
axX.set_ylabel('Posición')

axM.set_xlim((-2,2))
axM.set_ylim((-2,2))
axM.set_xlabel('Posición X')
axM.set_ylabel('Posición Y')

axA.set_xlim((0,5))
axA.set_ylim((-.5,2))
axA.set_xlabel('Frecuencia ($\Omega$)')
axA.set_ylabel('Amplitud')
axA.grid()

omega = 2
omegavar = np.linspace(0,5,500)
t = 0 
tvar = np.linspace(0,10,500)

A,B,X = posicion(t,omega)
_,_,Xv = posicion(tvar,omega)
Av,Bv,_ = posicion(t,omegavar)
axA.plot(omegavar,np.sqrt(Av**2 + Bv**2),lw=2,color = 'k',ls = '--')

lineX, = axX.plot(tvar,Xv)
lineM, = axM.plot(X, 0, 'o',ms = 15,zorder = 1)
lineRes, = axM.plot([-2,X],[0,0],ls = '--',color = 'k', lw = 2,zorder = 0)
lineA, = axA.plot(omega,np.sqrt(A**2 + B**2), 'o', ms = 15)

## Todo el tiempo corre la función auto_update
anim = animation.FuncAnimation(fig,auto_update, interval = 100,frames = int(2*np.pi/omega/0.4))

# Cuando se actualice el slider omega correr la función update
sli_omega.on_changed(update)

plt.show()
