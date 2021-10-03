#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:33:01 2021

@author: tobias
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti , tfadd ,tfcascade
import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt
%matplotlib qt5
#alfa_max = 3    #INPUT
#ws = 10         #INPUT
#wp = 1          #INPUT
#n = 3           #INPUT    
#ee = 10**(alfa_max/10) - 1
#wb = wp * (np.sqrt(ee))**(-1/n)
#w1 = wp * wb
#w2 = wp * wb
#k = wb **2
#q1 = 1/(2*np.cos(np.pi/8))
#q2 = 1/(2*np.cos(3*np.pi/8))

k = 1/2
num1 = [k,k]
den1 = [1 , 6 , 8]





tf1 = sig.TransferFunction(num1,den1)


analyze_sys( [tf1], ["Test" ])