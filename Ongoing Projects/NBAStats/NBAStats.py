#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:35:49 2019

@author: guilhermetheis
@license: MIT
@description: this is a web scrapper that saves the stats of the NBA games 
"""

#------------ Imports ------------#

import pandas as pd #data organization
import numpy as np #data processing
from matplotlib import pyplot as plt #plotting
import seaborn as sns #statistics
from urllib.request import urlopen #to open URL
from bs4 import BeautifulSoup #to extract dat from HTML

#------------ URL init ------------#


url = "http://www.espn.com/nba/scoreboard" #creating string to use
html = urlopen(url)
