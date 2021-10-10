#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:11:12 2021

@author: tobias
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from schemdraw import Drawing
from schemdraw.elements import Resistor, Capacitor, Inductor, Line, Dot

def to_latex (unsimbolo) :
    return('$' + sp.latex(unsimbolo)+ '$')

s = sp.symbols('s', complex = True)

sigma1 = 1
TV = ((s+1))/( (s+2)*(s+4) )                    # Transfer function
z11 = ((s+2)*(s+4))/((s+1)*(s+3))                 

k1 = sp.limit((s+1)*z11 , s , -sigma1 )
print(k1)                   #Residuo del tanque RC
c1 = 1/k1
r1 = sigma1/k1
print("C1 = ",c1,"\t","R1 = ",r1)

z3 = sp.factor(sp.simplify(sp.expand(z11 - k1/(s+sigma1))))
print(z3)
r2 = k1 = sp.limit(z3 , s , sp.oo )
print(r2)                   #Residuo del R serie
print("R2 = ", r2)

y5 = 1/sp.factor(sp.simplify(sp.expand(z3 - r2)))
print(y5)
k3 = sp.limit(y5/s , s , sp.oo )
print(k3)
print("C3 = ", k3)

k4 = 1/sp.factor(sp.simplify(sp.expand(y5 - s*k3)))
print(k4)
print("R4 = ",k4)

#d = Drawing(unit=4)

#d += Dot()
#d += Resistor().label(to_latex(r1))
#d.draw()
y22 = ((s+4)*(s+2))/((s+3))

sigma1 = 1
r0 = 1/sp.expand(y22).subs(s,-sigma1)
yc = sp.factor(sp.simplify(sp.expand(y22 - 1/r0)))
print(r0)
print(yc)

k2 = sp.limit(((s+1)/yc), s , -sigma1 )
print(k2)                   #Residuo del tanque RC
c2 = 1/k2
r2 = sigma1/k2
print("C1 = ",c2,"\t","R1 = ",r2)

ye = 1/sp.factor(sp.simplify(sp.expand(1/yc - k2/(s+sigma1))))
print(ye)
k3 = sp.limit(ye/s , s , sp.oo )
print(k3)
print("C3 = ", k3)

r4 = 1/sp.factor(sp.simplify(sp.expand(ye - s*k3)))
print("R4 = ", r4)
