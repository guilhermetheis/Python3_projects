#!/usr/bin/env python3

"""
This paste a clipboard list and add a * to it, after
that it copy this to the clipboard
"""

import sys, pyperclip

text = pyperclip.paste()

# Separate lines 
lines = text.split('\n')
# Adding *
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

out_list = '\n'.join(lines)

pyperclip.copy(out_list)
