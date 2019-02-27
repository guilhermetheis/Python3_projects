#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:35:49 2019

@author: guilhermetheis
@license: MIT
@description: this is a web scrapper to learn how to do that

Based on the https://www.datacamp.com/community/tutorials/web-scraping-using-python tutorial
"""

#------------ Imports ------------#

import pandas as pd #data organization
import numpy as np #data processing
from matplotlib import pyplot as plt #plotting
import seaborn as sns #statistics
from urllib.request import urlopen #to open URL
from bs4 import BeautifulSoup #to extract dat from HTML

#------------ URL init ------------#


url = "http://www.hubertiming.com/results/2017GPTR10K" #creating string to use
html = urlopen(url)

#------------ SOUP ------------#

soup = BeautifulSoup(html, 'lxml')

title = soup.title
#print(title)
text = soup.get_text()
#print(soup.text)

all_links = soup.find_all('a') #extracting the hyperlinks (in HTML <a> is for link)
#for link in all_links:
#    print(link.get("href")) # to truly print only the hyperlinks
#print(hyperlinks)

rows = soup.find_all('tr') # table rows (tr argument)
#print(rows[:10]) #only 10 for sanity

list_rows = []

for row in rows:
    row_td = row.find_all('td') #convert the rows in dataframes
    str_cells = str(row_td) #transforming the row_td into a string
    cleantext = BeautifulSoup(str_cells, "lxml").get_text() #this extracts the text from str_cells without the HTML tags
    list_rows.append(cleantext)

#print(row_td)
#type(row_td)

#print(cleantext)

df = pd.DataFrame(list_rows)
#print(df.head(10)) #printing the 10 first rows
df1 = df[0].str.split(',', expand=True)
df1[0] = df1[0].str.strip('[')
print(df1.head(10))

