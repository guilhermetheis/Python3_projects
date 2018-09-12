#!/usr/bin/env python3

"""
Author: Guilherme Theis

License: MIT

Email: guilhermetheis15@gmail.com

Github: https://github.com/guilhermetheis
"""

"""
Description: 
Usage:  
"""

# Imports

import numpy as np 
import os, argparse # In case of need
import matplotlib.pyplot as plt # for plotting
import tkinter
from scipy import signal # For transfer functions

num = [1, 1] # numerator
den = [1, 1, 1] # denominator

H = signal.TransferFunction(num, den) #creating the TF

#print(H) #verifying TF

w, mag, phase = signal.bode(H) # generating frequency for plot, mag and phase

#Verifying outputs

#print(w)
#print(mag)
#print(phase)


plt.figure()
plt.plot(w, phase)
plt.figure()
plt.plot(w, mag)
plt.show()