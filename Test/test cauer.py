
"""
Created on Tue Nov  9 06:50:42 2021

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

s = sp.symbols('s', complex = True)

# z = ((s**2+1)*(s**2+3)) / (s*(s**2+2))
# (z2,kinf) = spl.remover_polo_infinito(z)
# print(z2,kinf)

# (y4,kinf) = spl.remover_polo_infinito(1/z2)
# print(y4,kinf)

# (z6,kinf) = spl.remover_polo_infinito(1/y4)
# print(z6,kinf)

# (z8,k0) = spl.remover_polo_dc(z6)
# print(z8,k0)
################

y22 = (s**2+s*9/4)/(s+2)

(y2,kinf) = spl.remover_polo_infinito(y22)
print(y2,kinf)

(z4,k0) = spl.remover_polo_dc(1/y2,1)
print(z4,'-x-',k0)