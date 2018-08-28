#!/usr/bin/env python3

# For pytube installation pip3 install pytube

# Argparse allows to add the url from command line
import os, argparse

from pytube import YouTube

# Creating the argparse

parser = argparse.ArgumentParser()

# Allows inputs from bash

parser.add_argument ('-url', required =True) # IP Address
parser.add_argument ('-path', required =True) # IP Address
args = parser.parse_args() 

# Creating a yt object

yt = YouTube(args.url)

#print(yt.title) # Verifying if correctly connected with argparse

#Chosing the quality of the video (first always higher quality)

stream = yt.streams.first()

#print(stream) # Veryfing stream

# Print to know which video you're downloading

print('Downloading ' + yt.title + " from YouTube url: " + args.url)

# Downloading the video (best quality)

stream.download(args.path)

