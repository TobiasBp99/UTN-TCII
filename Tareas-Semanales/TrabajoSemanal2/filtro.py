#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: toto
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import control.matlab as ml
#from matplotlib import pyplot as plt


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

#%%Selecciono componentes normalizados
K = 10
Q = 10
R1 = 1/K
R2 = Q
R3 = 1
C = 1
R4 = 1

W01 = 1/(C*R3)
K1 = R3/R1
Q1 = R2/R3

num1 = np.array([ K1*W01 ])
den1 = np.array([ 1, W01/Q1 , W01**2])
#%%Armo TF lowpass
H1 = ml.tf( num1, den1 )
print(H1)
print("Pole:",ml.pole(H1),"Zero:",ml.zero(H1))



fig1 = plt.figure()
mag,pahse,w =ml.bode(H1)
plt.show()

fig2 = plt.figure()
fig2 = ml.pzmap(H1, plot=True,grid=False)
unit = plt.Circle((0, 0), 1, color='b', fill=False, ls = '-' , lw = 0.25)
plt.gca().add_patch(unit)
#%%Armo TF bandpass
K2 = - R2/R1
num2 = np.array([ K2*(W01/Q1) , 0 ])
print(num2)
den2 = np.array([1 , W01/Q1 , W01**2 ])

H2 = ml.tf( num2, den2 )
print(H2)
print("Pole:",ml.pole(H2),"Zero:",ml.zero(H2))



fig3 = plt.figure()
mag,pahse,w =ml.bode(H2)
plt.show()

fig4 = plt.figure()
fig4 = ml.pzmap(H2, plot=True,grid=False)
unit = plt.Circle((0, 0), 1, color='b', fill=False, ls = '-' , lw = 0.25)
plt.gca().add_patch(unit)
#%%Butter
#Solo modifico R2
R2 = np.sqrt(2)/2
W01 = 1/(C*R3)
K1 = R3/R1
Q1 = R2/R3

num1 = np.array([ K1*W01 ])
den1 = np.array([ 1, W01/Q1 , W01**2])
H3 = ml.tf( num1, den1 )
print(H3)
print("Pole:",ml.pole(H3),"Zero:",ml.zero(H3))



fig5 = plt.figure()
mag,pahse,w =ml.bode(H3)
plt.show()

fig2 = plt.figure()
fig2 = ml.pzmap(H3, plot=True,grid=False)
unit = plt.Circle((0, 0), 1, color='b', fill=False, ls = '-' , lw = 0.25)
plt.gca().add_patch(unit)

