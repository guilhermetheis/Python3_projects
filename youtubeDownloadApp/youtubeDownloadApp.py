#!/usr/bin/env python3

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

#print(yt.title) # Verifying if correctly connected with argparse

# Chosing the quality of the video (first always higher quality)

stream = yt.streams.filter(only_audio=args.mp3).first()

#print(stream) # Veryfing stream

# Print to know which video you're downloading

print('Downloading ' + yt.title + " from YouTube url: " + args.url)

# Downloading the video (best quality)

stream.download(args.path)
print('File name :'+stream.default_filename) # Verifying if filename works

# Changing extension to mp3
p = Path('videos/'+stream.default_filename)
p.rename(p.with_suffix('.mp3'))