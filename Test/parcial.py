# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:23:48 2021

@author: toto_
"""

import scipy.signal as sig
import matplotlib as mpl
from splane import analyze_sys, pretty_print_lti , tfadd ,tfcascade
import splane as spl
import numpy as np
import control.matlab as control
import matplotlib.pyplot as plt
import sympy as sp

%matplotlib qt5