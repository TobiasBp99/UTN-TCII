#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 08:57:49 2021

@author: tobias
"""



import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import control.matlab as ml
import scipy.signal as sig
from splane import analyze_sys,pzmap,grpDelay,bodePlot, pretty_print_lti

%matplotlib qt5



alfa_max    = 0.4

ws  = 3

ee  = 10**(alfa_max/10)-1
print("eps^2 {:f}".format(ee))

for nn in range(2,8):
    alfa_min_b  =   10*np.log10(1 + ee*ws**(2*nn))   
    alfa_min_c  =   10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 )
    print("nn {:d} -> alfa:min_butter {:f}  - alfa:min_cheby {:f}".format(nn,alfa_min_b,alfa_min_c))
    
#z,p,k = sig.buttap(nn)

#num, den = sig.zpk2tf(z,p,k)
#num, den = sig.lp2lp(num, den, ee**(-1/2/nn))

# verificación Cheby

print("Polo\t:",np.roots([ 4.969 , 6.0207 , 10.089 , 7.113 , 4.078 , 1 ]))

n = 5 

z,p,k = sig.cheb1ap(n, alfa_max)

print("Zero\t:",z)
print("Pole\t:",p)
print("K\t:",k)

num,den = sig.zpk2tf(z,p,k)

print("Num\t:",num)
print("Den\t:",den)

this_lti = sig.TransferFunction(num,den)


pretty_print_lti(this_lti)

analyze_sys([this_lti], 'Cheby n=5')

