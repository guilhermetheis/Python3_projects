#!/usr/bin/env python3
'''
This is a python based generic RF calculator to both automatize some of my work as RF engineer
'''
__date__ = "30/03/2019"
__author__ = "Guilherme Theis"
__copyright__ = "Copyright 2019, GTheis"
__credits__ = []
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Guilherme Theis"
__email__ = "Guilherme Theis"
__status__ = "Development"

# Imports
import numpy as np

class Calculator:
    
    #def __init__(): #constructor

    def mW2dBm(mWVal):
        return 10*np.log10(mWVal) #converts mW to dBm
    def W2dBm (WVal):
        return 10*np.log10(WVal/1E-3) #converts W to dBm
    def dBm2W(dBmVal):
        return (10**(dBmVal/10))*1E-3 #converts dBm to W
    def dBm2mW(dBmVal):
        return 10**(dBmVal/10) #converts dBm to W

def main():
    #Main function mostly for tests as of right now

if __name__ == "__main__":
    main()