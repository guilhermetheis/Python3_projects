#!/usr/bin/env python3

def imagePrinting(grid):
	numbRows = len(grid) 
	numbColums = len(grid[0]) 
	for j in range(numbColums):
		for i in range(numbRows):
			if i == (numbRows - 1):
				print(grid[i][j])
			else:
				print(grid[i][j], end='')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

imagePrinting(grid)
