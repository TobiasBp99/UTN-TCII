# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:16:00 2021

@author: toto_
"""
import numpy as np
def Pre_Warp(fo, e):
    w_d = 0
    w_a = 0
    fs = fo
    w_d = 2*np.arctan(np.pi*fo/fs)
    w_a = w_d*fs/(2*np.pi)
    print(w_d,w_a)
    while(w_a < fo*e):
        fs = fs + 1
        w_d = 2*np.arctan(np.pi*fo/fs)
        w_a = w_d*fs/(2*np.pi)
    return(fs,w_a,w_d)

print(Pre_Warp(2000, 0.95))