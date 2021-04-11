# -*- coding: utf-8 -*-
"""
Autor   :  Tobias Bavasso Piizzi
Fecha   :   11/04/21

Gráfico de módulo y fase circuito girador
"""


from sympy import (
    init_printing, symbols, arg, I, plot, pi, 
    lambdify, Heaviside, exp
)
init_printing()

s = symbols("s")
w = symbols("omega", real=True)

R1 = 1e3
R2 = 1e3
R3 = 1e3
R4 = 1e3
C1 = 1e-6

Z = -s*C1*R1*R2*R4/R3
Z

Zw = Z.subs(s, I*w)
Zw

mod = abs(Zw)
phi = arg(Zw)


plot(mod, (w, 0.01, 100), xscale="log", yscale="log",
     ylabel="|Z(w)|", xlabel="$\omega$")

plot(phi*180/pi, (w, 0.01, 100), xscale="log", 
     xlabel="$\omega$", ylabel="$\phi$")