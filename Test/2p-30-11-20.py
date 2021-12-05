# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:16:31 2021

@author: toto_
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti , tfadd ,tfcascade
import splane as spl
import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt
import sympy as sp

%matplotlib qt5
k = 1
num1 = [k,0,4*k,0]
den1 = [1,2,2,1]
tf1 = sig.TransferFunction(num1,den1)

analyze_sys( [tf1], ["Test" ])

s = sp.symbols('s', complex = True)

za = (s*(s**2+2)) / (2*(s**2+1/2))

(zc,k0) = spl.remover_polo_dc(1/za)

print(zc,'-----',k0)