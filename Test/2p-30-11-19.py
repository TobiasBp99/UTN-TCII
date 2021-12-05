# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:41:37 2021

@author: toto_
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti , tfadd ,tfcascade
import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt
import sympy as sp

%matplotlib qt5


num1 = [1,0,0,0]
den1 = [1,3,3,1]
tf1 = sig.TransferFunction(num1,den1)

analyze_sys( [tf1], ["Test" ])

s = sp.symbols('s', complex = True)

r = 1
zl2 = s*3
zc3 = 1/(s*8/9)
zl3 = s*3/8

z11 = 1/((1/r)+(1/zl2)+(1/(zc3+zl3)))

print(sp.simplify(z11))