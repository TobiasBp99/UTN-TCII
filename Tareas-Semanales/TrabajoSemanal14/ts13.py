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

h = 1/2
#num1 = [1 , 5 , 4]
#den1 = [1,8,12]



num2 = [1*h , 5*h , 4*h]
den2 = [1,8,12]



#tf1 = sig.TransferFunction(num1,den1)
tf2 = sig.TransferFunction(num2,den2)

#analyze_sys( [tf1], ["Sin H" ])
analyze_sys( [tf2], ["-I2 / I1" ])