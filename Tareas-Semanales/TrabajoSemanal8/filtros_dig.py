# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 08:37:31 2021

@author: toto_
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti , tfadd ,tfcascade
import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt
import sys
%matplotlib qt5

# num1 = [1]
# den1 = [1,1,1]
# tf1 = sig.TransferFunction(num1,den1)


# num2 = [1]
# den2 = [1,1]
# tf2 = sig.TransferFunction(num2,den2)


# tf = tfcascade(tf1, tf2)    #Hasta acá como siempre, hago mi filtro analógico

num_a = [1]
den_a = [1,2,2,1]

fs = 40                    #Selecciono mi frecuencia de sampleo = fs/W   

num_z, den_z = sig.bilinear(num_a, den_a, fs)
print(num_z)
print(den_z)

tf_z = sig.TransferFunction(num_z, den_z, dt=1/fs)

analyze_sys([tf_z], "Digitales")
