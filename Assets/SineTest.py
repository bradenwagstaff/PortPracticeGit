from cmath import pi
import numpy as np
import sys

var = pi/24

for i in range (24):
    amplitude   = np.sin(i * var)
    print(amplitude)

