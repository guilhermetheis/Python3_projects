#!/usr/bin/env python3
'''
This is a python program that creates a header for my future programs.

'''
__date__ = "02/04/2019"
__author__ = "Guilherme Theis"
__copyright__ = "Copyright 2019, GTheis"
__credits__ = []
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Guilherme Theis"
__email__ = "guilhermetheis.pro@gmail.com"
__status__ = "Development"

# Imports
import os, argparse
import time

parser = argparse.ArgumentParser()

# Arguments from parser

parser.add_argument ('-p', '--path',help='file path ', required =True, type=str)
parser.add_argument ('-l','--language',help='programming languague used', required =True, type=str)
parser.add_argument('-f', '--file', help='name of the file', type=str)
args = parser.parse_args() 

file = open(args.path+args.file, 'w')
file.write("\'\'\'\n")
file.write("brief description\n")
file.write("\'\'\'\n")
file.write("__date__ = "+"\""+time.strftime("%d/%m/%Y")+"\"\n")
file.write("__author__ = \"Guilherme Theis\"\n")
file.write("__copyright__ = \"Copyright 2019, GTheis\"\n")
file.write("__credits__ = []\n")
file.write("__license__ = \"MIT\"\n")
file.write("__version__ = \"0.0.1\"\n")
file.write("__maintainer__ = \"Guilherme Theis\"\n")
file.write("__email__ = \"Guilherme Theis\"\n")
file.write("__status__ = \"Development\"\n")
file.write("\n\n\n")
file.write("# Imports\n")
file.write("\n\n\n")
file.write("def main():\n")
file.write("\n\n\n")
file.write("if __name__ == \"__main__\":\n")
file.write("\tmain()")
file.close()

