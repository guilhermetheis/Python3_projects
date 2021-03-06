#!/usr/bin/env python3

"""
Author: Guilherme Theis

License: MIT

Email: guilhermetheis15@gmail.com

Github: https://github.com/guilhermetheis

Usage: to use this program you need to run a 
./youtubeDownloadApp.py -url enter.url.com -path "path" -mp3 True
for a mp3 generation, for an mp4 the -mp3 should be false
"""

# For pytube installation pip3 install pytube

# Argparse allows to add the url from command line
import os, argparse

from pytube import YouTube
from pathlib import Path
from tqdm import tqdm

# Creating the argparse

parser = argparse.ArgumentParser()

# Allows inputs from bash

parser.add_argument ('-url', required =True) # URL  
parser.add_argument ('-path', required =True) # Path to save
parser.add_argument ('-mp3', required=True, type=bool)

args = parser.parse_args() 

# Creating a yt object

yt = YouTube(args.url)

#print(yt.title) # Verifying if correctly recognizes the video with argparse

# Chosing the quality of the video (first always higher quality)

stream = yt.streams.filter(only_audio=args.mp3).last() # Taking the worst quality to faster download



#print(stream) # Veryfing stream

# Print to know which video you're downloading

print('Downloading ' + yt.title + " from YouTube url: " + args.url)
# Downloading the video (best quality)

stream.download(args.path)
print('File name :'+stream.default_filename) # Verifying if filename works
