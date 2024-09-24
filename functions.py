#---¡THIS-CONTAINS-A-FUCNTION-TO-CALCULATE-THE-ROOTS!

#---¡IMPORT-LIBRARIES!
import numpy as np

#---¡CONSTANTS-OF-THE-FUNCITON!
L = 10#ft
r = 1#ft
V = 12.4#ft**3
C = V / (L*r**2) - 0.5*np.pi 

#---¡FUNCTION!
def f(x):
    return np.arcsin(x) + x*(1-x**2)**(1/2) + C

#---¡FIRST-DERIVATIVE-DERIVATIVE-OF-THE-FUNCTION!
def df(x):
    return 2*(1-x**2)**(1/2)

#---¡CALCULATE-h-VALUE!
def H(x):
    return x*r

#---¡CALCULATE-DEPTH-OF-THE-WATER!
def DEPTH(h):
    return r - h