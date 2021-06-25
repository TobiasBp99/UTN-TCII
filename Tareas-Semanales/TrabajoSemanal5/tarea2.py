#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:41:05 2021

@author: tobias
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti
import numpy as np
%matplotlib qt5



z = [3j , -3j]
p = [-1 , ((-1/2) + 1j*np.sqrt(3)/2) , ((-1/2) -1j*np.sqrt(3)/2) ]
k = 1/9

num,den   = sig.zpk2tf(z,p,k)
tf   = sig.TransferFunction(num,den)

#pretty_print_lti([tf])
#analyze_sys( [tf], ["LowPass Normalizado" ])


num_hp,den_hp = sig.lp2hp(num, den)
tf_hp   = sig.TransferFunction(num_hp,den_hp)

analyze_sys( [tf_hp], ["HighPass Normalizado" ])
pretty_print_lti([tf]_hp)