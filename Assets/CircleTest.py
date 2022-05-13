import numpy as np
from cmath import pi

import matplotlib.pyplot as plot

import sys

 

# Get x values of the sine wave

time        = np.arange(0, pi * 2, 0.1)

 

# Amplitude of the sine wave is sine of a variable like time

amplitude   = np.sin(time)

 

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(time, amplitude)

 

# Give a title for the sine wave plot

plot.title('Sine wave')

 

# Give x axis label for the sine wave plot

plot.xlabel('Time')

 

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

 

plot.grid(True, which='both')

 

plot.axhline(y=0, color='k')

 

plot.show()

 

# Display the sine wave

plot.show()