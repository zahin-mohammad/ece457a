from numpy import cos, exp
from math import pi

INTERVAL = (-100, 100)


# Easom function f : [-100,100]^2 -> R
def f(x):
    x1, x2 = x

    return -cos(x1) * cos(x2) * exp(-(x1-pi)**2 - (x2-pi)**2)
