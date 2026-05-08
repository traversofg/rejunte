import numpy as np
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from functools import partial
from matplotlib.animation import FuncAnimation
from matplotlib import rc

rc('animation')

### PARAMETROS GLOBALES

G = 9.8066 # en mayus porque queda cte siempre

L_0 = 0.5

L = 0.5 # Longitud del pendulo en m

masa = 1.0

k_el = 0.9


### FRECUENCIAS DE CADA MODO ###

w1 = np.sqrt(G/L)

w2 = np.sqrt(G/L + 2*k_el/masa)

### FUNCIONES PRINCIPALES

def ecuacion_de_movimiento(longitud, amplitud_ini, t):
    pass
    # return amplitud_ini * np.sin( t * np.sqrt(G/longitud) )


def update(t):

    pass

### FIGURA PRINCIPAL

# fig, ax = plt.subplots()

# ax.set_xlim(-.2, .7)
# ax.set_ylim(-.1, .6)

# ax.set_xlabel('Posición')
# ax.set_title(f'Pendulo en modo {1}') # Despues veo como hacer para que el titulo represente bien el n° de modo

# with mpl.rc_context({'path.sketch': (5, 15, 1)}):
#     line1, = ax.plot([], [], color = 'black') # Esta une ambas masas, sería el resorte

# line2, = ax.plot([], [], 'b-')  # Pendulo masa izq
# line3, = ax.plot([], [], 'b-')  # Pendulo masa der

# plt.grid()

""" Intento de hacerlo un poco mas "automatizado" pero no salió (por ahora)
def func(frame, var1, var2):

    x = [var1[frame], 0.5 + var2[frame]]
    y = [0, 0]

    line1.set_data(x,y)

    line2.set_data([0, var1[frame]], [L, 0])
    line3.set_data([0, var2[frame]], [L, 0])

    return line1, line2, line3

def animate(var1, var2, t, w):
    ani = animation.FuncAnimation(
        fig, partial(func, var1, var2),
        frames=len(t), interval=2*np.pi/w, blit=True)
    plt.show()

### MODO 1 ###
    
t1 = np.linspace(0,2*pi/w1, 1024)

amp_ini = 0.05

psi_a1 = amp_ini * cos(w1*t1)
psi_b1 = psi_a1

animate(psi_a1, psi_b1, t1, w1)

plt.show()
"""

### Figura principal

fig, ax = plt.subplots()

ax.set_xlim(-.2, .7)
ax.set_ylim(-.1, .6)

ax.set_xlabel('Posición')
ax.set_title('Pendulo en modo normal') # Despues veo como hacer para que el titulo represente bien el n° de modo

with mpl.rc_context({'path.sketch': (5, 15, 1)}):
    line1, = ax.plot([], [], color = 'black') # Esta une ambas masas, sería el resorte
    
line2, = ax.plot([], [], 'b-')  # Pendulo masa izq
line3, = ax.plot([], [], 'b-')  # Pendulo masa der

masita1, = ax.plot([],color='black', marker='o')
masita2, = ax.plot([],color='black', marker='o')

plt.grid()


### Modo 1:

t1 = np.linspace(0,2*pi/w1, 512)

amp_ini = 0.05

def func_1(frame):

    psi_a1 = amp_ini * cos(w1*t1)
    psi_b1 = psi_a1

    var1 = psi_a1
    var2 = psi_b1

    masita1.set_data([var1[frame]], [0,0])
    masita2.set_data([0.5 + var2[frame]], [0,0])

    x = [var1[frame], 0.5 + var2[frame]]
    y = [0, 0]

    line1.set_data(x,y)

    line2.set_data([0, var1[frame]], [L, 0])
    line3.set_data([0.5, 0.5 + var2[frame]], [L, 0])

    return line1, line2, line3, masita1, masita2

# ani1 = FuncAnimation(fig, func_1, frames=len(t1),
                    #  interval= 2*pi/w1, blit=True)

# plt.show()

### Modo 2:

t2 = np.linspace(0,2*pi/w2, 256)

amp_ini = 0.05

psi_a2 = amp_ini * cos(w2*t2)
psi_b2 = -psi_a2

var1 = psi_a2
var2 = psi_b2

def func_2(frame):

    x = [var1[frame], 0.5 + var2[frame]]
    y = [0, 0]

    line1.set_data(x,y) # Dibuja el resorte entre masitas

    line2.set_data([0, var1[frame]], [L, 0])
    line3.set_data([0.5, 0.5 + var2[frame]], [L, 0])

    masita1.set_data([var1[frame]], [0,0])
    masita2.set_data([0.5 + var2[frame]], [0,0])

    return line1, line2, line3, masita1, masita2

ani2 = FuncAnimation(fig, func_2, frames=len(t2),
                     interval= 2*pi/w2, blit=True)

plt.show()