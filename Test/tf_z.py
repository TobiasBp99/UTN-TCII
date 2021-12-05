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

k = 1
#num1 = [1,0,4,0]
#den1 = [1,2,2,1]
# num1 = [k,0,4*k]
# den1 = [1,2,2,1]

num1 = [0.8,0,0,0,1]
den1 = [1,0,0,0,0.8]
tf1 = sig.TransferFunction(num1,den1,dt=1)

# # w, mag, phase = sig.dbode(tf1)
# # plt.figure()
# # plt.semilogx(w, mag)    # Bode magnitude plot
# # plt.figure()
# # plt.semilogx(w, phase)  # Bode phase plot

# w, h = sig.freqz(num1,den1)

# fig, ax1 = plt.subplots()
# ax1.set_title('Digital filter frequency response')
# ax1.plot(w, 20 * np.log10(abs(h)), 'b')
# ax1.set_ylabel('Amplitude [dB]', color='b')
# ax1.set_xlabel('Frequency [rad/sample]')
# ax2 = ax1.twinx()
# angles = np.unwrap(np.angle(h))
# ax2.plot(w, angles, 'g')
# ax2.set_ylabel('Angle (radians)', color='g')
# ax2.grid()
# ax2.axis('tight')
# plt.show()
analyze_sys( [tf1], ["Test"])
#plt.show()