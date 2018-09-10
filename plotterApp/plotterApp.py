#!/usr/bin/env python3

"""
Author: Guilherme Theis

License: MIT

Email: guilhermetheis15@gmail.com

Github: https://github.com/guilhermetheis
"""

import os, argparse, csv

parser = argparse.ArgumentParser()

# Allows inputs from bash

parser.add_argument ('-usedFile', required=True)#file to be opened

args = parser.parse_args() 

#print(args.usedFile) #verifying if argparse worked

with open(args.usedFile) as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	varList = list(spamreader)

newVarList1 = [row[0].split(",")[0] for row in varList] # tunning the data
newVarList2 = [row[0].split(",")[1] for row in varList]

#print(newVarList1) #veryfing output of loop
#print(newVarList2) #veryfing output of loop

plotable


