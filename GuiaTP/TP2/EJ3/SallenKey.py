#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:48:32 2021

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

#%%1ºCelda
#Selecciono los componentes
R1  = 1
RB1  = 0.068
C1   = 1   

W01 = 1/(C1*R1)
K1 = 1 + RB1/R1
Q1 = 1/(3-K1)

num1 = np.array([ K1*W01 ])
den1 = np.array([ 1, W01/Q1 , W01**2])

#%%2ºCelda
#Selecciono los componentes
R2  = 1
RB2  = 0.58
C2   = 1   

W02 = 1/(C2*R2)
K2 = 1 + RB2/R2
Q2 = 1/(3-K2)

num2 = np.array([ K2*W02 ])
den2 = np.array([ 1, W02/Q2 , W02**2])

#%%3ºCelda
#Selecciono los componentes
R3  = 1
RB3  = 1.48
C3   = 1   

W03 = 1/(C3*R3)
K3 = 1 + RB3/R3
Q3 = 1/(3-K3)

num3 = np.array([ K3*W03 ])
den3 = np.array([ 1, W03/Q3 , W03**2])

#%%

H1 = ml.tf( num1, den1 )
print("Pole:",ml.pole(H1),"Zero:",ml.zero(H1))
H2 = ml.tf( num2, den2 )
print("Pole:",ml.pole(H2),"Zero:",ml.zero(H2))
H3 = ml.tf( num3, den3 )
print("Pole:",ml.pole(H3),"Zero:",ml.zero(H3))

num_a =np.polymul(num1,num2)
num_t = np.polymul(num_a,num3)

den_a =np.polymul(den1,den2)
den_t = np.polymul(den_a,den3)

HT = ml.tf( num_t,den_t)
print("Pole:",ml.pole(HT),"Zero:",ml.zero(HT))

fig1 = plt.figure()
fig1.suptitle("Celda 1")
mag,pahse,w =ml.bode(H1)
fig2 = plt.figure()
fig2.suptitle("Celda 2")
mag,pahse,w = ml.bode(H2)
fig3 = plt.figure()
fig3.suptitle("Celda 3")
mag,pahse,w = ml.bode(H3)
fig4 = plt.figure()
fig4.suptitle("Filtro")
mag,pahse,w = ml.bode(HT)
plt.show()

fig5 = plt.figure()
ml.pzmap(HT, plot=True,grid=True)







