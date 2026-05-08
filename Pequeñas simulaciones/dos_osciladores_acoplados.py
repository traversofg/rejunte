from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib as mpl


### Parametros generales

m = 1 # Por ahora laburo con masas iguales para no complicarme la vida

k_el_muelles = 10
k_el_union = 2.5

pos_ini_a = -2.5
pos_ini_b = 2.5

vel_ini_a = 0
vel_ini_b = 0

w1 = sqrt(k_el_muelles/m)
w2 = sqrt((k_el_muelles + 2 * k_el_union) / m)

t = linspace(0, 2*pi*w1, 512)

A = .5
B = 1

### Frecuencias del batido

w_prom = (w2 + w1) / 2

w_mod = (w2 - w1) / 2

t = linspace(0, 2*pi/w_mod, 1024)

### Ecuaciones de movimiento (con un corrimiento para graficar)

psi_a = A*sin(w_prom*t)*sin(w_mod*t) + pos_ini_a

psi_b = A*cos(w_prom*t)*cos(w_mod*t) + pos_ini_b

### Gráfico de frecuencias (sacado del codigo de Cande)

total = sin(w_prom*t)*sin(w_mod*t)
oscilacion_rapida = sin(w_prom*t)
amplitud_modulada = sin(w_mod*t)
amplitud_modulada2 = -sin(w_mod*t)
# plt.figure(figsize=(10,6))
# plt.plot(t,total, linewidth = 2, label="total")
# plt.plot(t,oscilacion_rapida, "--", linewidth=0.8, label="rápida")
# plt.plot(t,amplitud_modulada,"--", linewidth=3, label="modulación")
# plt.plot(t,amplitud_modulada2,"--", linewidth=3)
# plt.legend(loc=9)
# plt.show()

### Figura principal

fig, ax = plt.subplots(figsize=(9, 4))

ax.set_title('2 osciladores acoplados')
ax.set_xlim(-5,5)
ax.set_ylim(-1,1)

ax.vlines(x=0, ymin=-2, ymax=2, colors='grey',
          linestyles='dashed', linewidth=.75)

ax.vlines(x=pos_ini_a, ymin=-2, ymax=2, colors='grey',
          linestyles='dashed', linewidth=.75)

ax.vlines(x=pos_ini_b, ymin=-2, ymax=2, colors='grey',
          linestyles='dashed', linewidth=.75)

ax.hlines(y=0, xmin=-5, xmax=5, colors='grey',
          linestyles='dashed', linewidth=.75)

ax.set_xticks([pos_ini_a, 0, pos_ini_b])
ax.set_yticks([0])

ax.set_xticklabels(['$\psi_{a,0}$', 0, '$\psi_{b,0}$'])
ax.set_yticklabels([])
ax.text(-4.75, 0.75, f'K costados: {k_el_muelles}')
ax.text(-4.75, 0.50, f'K acoplamiento: {k_el_union}')

# ax.set_xlabel('Posicion')

mass1, = ax.plot([], [], 'bo', linewidth=2, markersize=7.5) # Masita izq

mass2, = ax.plot([], [], 'ro', linewidth=2, markersize=7.5) # Masita derecha

with mpl.rc_context({'path.sketch': (5, 15, 1)}): # Esto hace las lineas en zigzag cual resorte
    spring1, = ax.plot([],[], color='blue') # Resorte izquierda
    spring2, = ax.plot([],[], color='black') # Resorte de union
    spring3, = ax.plot([],[], color='red') # Resorte derecha

### Funcion para actualizar los datos

def update(frame):
    
    mass1.set_data([psi_a[frame]], [0,0])
    mass2.set_data([psi_b[frame]], [0,0])

    x1 = [ -5, psi_a[frame]]
    y1 = [0,0]
    spring1.set_data(x1,y1)
    
    x2 = [ psi_a[frame] , psi_b[frame] ]
    y2 = [0,0]
    spring2.set_data(x2,y2)

    x3 = [ psi_b[frame], 5]
    y3 = [0,0]
    spring3.set_data(x3,y3)

    return mass1, mass2, spring1, spring2, spring3

### Funcion para animar el movimiento

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

### Guarda la animación como GIF

writer = PillowWriter(fps=25,
                      metadata=dict(artist='Me'),
                      bitrate=1800)

ani.save('Batido resortes acop.gif', writer=writer)

plt.show()