#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:48:32 2021

@author: toto
"""
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from math import sqrt
# módulo de SciPy
from scipy import signal as sig

# un módulo adaptado a mis necesidades
from splane import bodePlot, pzmap
#%%  Inicialización de librerías
# Setup inline graphics: Esto lo hacemos para que el tamaño de la salida, 
# sea un poco más adecuada al tamaño del documento
mpl.rcParams['figure.figsize'] = (10,10)

#%% Esto tiene que ver con cuestiones de presentación de los gráficos,
# NO ES IMPORTANTE
fig_sz_x = 14
fig_sz_y = 13
fig_dpi = 80 # dpi

fig_font_family = 'Ubuntu'
fig_font_size = 16

plt.rcParams.update({'font.size':fig_font_size})
plt.rcParams.update({'font.family':fig_font_family})
#%%

#Selecciono los componentes
R1  = 1
R3  = 1
R4  = 1
C2  = 1 
C5  = 0.01
#%%Simulaciòn sin normalizar
k   = - R4/R1
w0  = 1/sqrt(C2*C5*R1*R3*R4)
q   = C2*R1*R3*R4/(sqrt(C2*C5*R1*R3*R4)*(R3*R4+R1*R4+R1*R3))


num = np.array([ k*w0**2])
den = np.array([ 1, w0/q , w0**2])


p = np.roots(num)
z = np.roots(den)

print("Polos",p)
print("Ceros",z)

H = sig.TransferFunction( num, den )
# Graficamos el diagrama de polos y ceros
# Graficamos la respuesta en frecuencia para el modulo y la fase.
_, axes_hdl = bodePlot(H)

# para que se vea como uno intuye el módulo. Probar comentar las siguientes 2 líneas
#plt.sca(axes_hdl[0])
#plt.ylim([-1,1])



plt.gca

pzmap(H)

plt.show()

#%% Simulaciòn normalizada
#norma_w = 100   #Valor calculado para normalizar
#norma_z = 2.1276e6

R1  = 2.1276e6
R3  = 2.1276e6
R4  = 2.1276e6
C2  = 4700e-12
C5  = 47e-12


k   = - R4/R1
w0  = 1/sqrt(C2*C5*R1*R3*R4)
print(w0)
q   = C2*R1*R3*R4/(sqrt(C2*C5*R1*R3*R4)*(R3*R4+R1*R4+R1*R3))

num_n = np.array([ k*w0**2])
den_n = np.array([ w0**2, w0/q , w0**2])


Hn = sig.TransferFunction( num_n , den_n )
# Graficamos el diagrama de polos y ceros
# Graficamos la respuesta en frecuencia para el modulo y la fase.
_, axes_hdl = bodePlot(Hn)

# para que se vea como uno intuye el módulo. Probar comentar las siguientes 2 líneas
#plt.sca(axes_hdl[0])
#plt.ylim([-1,1])

plt.gca

pzmap(Hn)

plt.show()

