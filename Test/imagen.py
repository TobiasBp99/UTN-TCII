# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti , tfadd ,tfcascade
import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt

at_db = 10
z1 = 100
z2 = 50

a = np.sqrt(z1/z2) * np.cosh(at_db/8.69)
b = np.sqrt(z1*z2) * np.sinh(at_db/8.69)
c = np.sinh(at_db/8.69) / np.sqrt(z1*z2) 
d = np.sqrt(z2/z1) * np.cosh(at_db/8.69)

z11 = a/c
z12 = a*d/c -b
z21 = 1/c
z22 = d/c

print(z11)
print(z12)
print(z21)
print(z22)