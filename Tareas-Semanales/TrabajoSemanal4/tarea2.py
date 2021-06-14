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

n1 = [ 1 , np.sqrt(2)/2 , 1 ]
n2 = [ 1 , 0 , 4]

p = [ 1 , np.sqrt(2) , 1]
k = 1

tf_be   = sig.TransferFunction(n1,p)
tf_n    = sig.TransferFunction(n2,p)

#pretty_print_lti(this_lti)

#analyze_sys( [tf_be], ["BE" ])

analyze_sys( [tf_n], ["Notch" ])