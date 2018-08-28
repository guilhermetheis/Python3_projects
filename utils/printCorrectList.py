#!/usr/bin/env python3

import string

def printTable(tableData):
	numbRows = len(tableData)
	numbColums = len(tableData[0]) 
	for j in range(numbColums):
		for i in range(numbRows):
			if i == (numbRows - 1):
				print(tableData[i][j].rjust(20))
			else:
				print(tableData[i][j].rjust(20), end='')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)