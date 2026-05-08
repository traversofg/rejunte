# -*- coding: utf-8 -*-
"""
Created on Fri May 30 01:06:00 2025

@author: FedeG
"""

import matplotlib.pylab as plt
import numpy as np

from scipy.integrate import solve_ivp 
from scipy.optimize  import root 

# ======= PARAMETROS Y VARIABLES DINAMICAS ======= #

G  = 9.8
L1 = 1.0
L2 = 1.0

L = L1

M1 = 1.0
M2 = 1.0


# ======= LA FISICA EN CUESTION ======= #

def deriv(t, phi):
    
    phi1, phi2, dphi1, dphi2 = phi
    
    M = M2 / (M1+M2)
    alfa = phi2 - phi1
    
    F1 = - (G/L) * np.sin(phi1) + M * dphi2**2 * np.sin(alfa)
    
    F2 = (G/L) * np.sin(phi2) + dphi1**2 * np.sin(alfa)
    
    def equations(accels):
        
        ddphi1, ddphi2 = accels
        
        eq1 = ddphi1 + ddphi2 * np.cos(alfa) * M - F1
        eq2 = ddphi2 - ddphi1 * np.cos(alfa) - F2
        
        return [eq1, eq2]
    
    roots = root(equations, [0,0])
    
    ddphi1, ddphi2 = roots.x
    
    return [dphi1, dphi2, ddphi1, ddphi2]

# ======= RESUELVO LAS ODES ======= #

# Condiciones iniciales

phi1_0 = 120.0
phi2_0 = -10.0

v1_0 = 0.
v2_0 = 0.

t_span = (0,2)
t_eval = np.linspace(*t_span, 1000) # 50 PPS

phi0 = [phi1_0, phi2_0, v1_0, v2_0]

sol = solve_ivp(
    fun=deriv, 
    t_span=t_span, 
    y0=phi0, 
    t_eval=t_eval,
    method='Radau'
    )

t = sol.t
phi1 = sol.y[0]
phi2 = sol.y[1]

# ======= GRAFICO A VER SI SALE ALGO ======= #

# =============================================================================
# x1 = L * np.sin(phi1)
# y1 = -L * np.cos(phi1)
# 
# x2 = x1 + L * np.sin(phi2)
# y2 = y1 - L * np.cos(phi2)
# 
# plt.plot(t, phi1)
# plt.plot(t, phi2)
# 
# plt.xlabel('tiempo')
# plt.ylabel('angulo')
# plt.legend([r'$\phi_{1}(t)$', r'$\phi_{2}(t)$'])
# plt.grid()
# 
# plt.show()
# =============================================================================

# Me aburri llego gpt pal grafico

# Extraigo variables
phi1 = sol.y[0]
phi2 = sol.y[1]
dphi1 = sol.y[2]
dphi2 = sol.y[3]
t = sol.t

# Conversion a coordenadas cartesianas
x1 = L * np.sin(phi1)
y1 = -L * np.cos(phi1)

x2 = x1 + L * np.sin(phi2)
y2 = y1 - L * np.cos(phi2)

# Subplots: ángulos y trayectorias
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: Ángulos
axs[0].plot(t, phi1, label=r'$\phi_1(t)$')
axs[0].plot(t, phi2, label=r'$\phi_2(t)$')
axs[0].set_xlabel('tiempo')
axs[0].set_ylabel('ángulo (rad)')
axs[0].grid()
axs[0].legend()
axs[0].set_title('Ángulos vs tiempo')

# Subplot 2: Trayectoria en el plano
axs[1].plot(x1, y1, label='Masa 1')
axs[1].plot(x2, y2, label='Masa 2')
axs[1].set_xlabel('x (m)')
axs[1].set_ylabel('y (m)')
axs[1].set_aspect('equal')
axs[1].grid()
axs[1].legend()
axs[1].set_title('Trayectoria espacial')

plt.tight_layout()
plt.show()
