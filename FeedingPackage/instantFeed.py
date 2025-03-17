#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:59:38 2020

@author: crystalhansen
"""

from lxml import html
import requests
import re 
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

 
dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

instagram = "https://www.instagram.com/zacklyrite/"

response = requests.get(instagram)
print(response.text)
soup = BeautifulSoup(response.text)
#print (soup)
fileN= "instagram/zsacklyrite" + d +".txt"

f=open(fileN,"w")
f.write(soup.title.string +"\n")
print(soup.title.string)
for li in soup.find_all('img'):
   
  
    #char = " "
    #replaceString = replace(li.text.strip(), char)
    #print(li.text.strip()+"; \n")
    
    f.write(li.text.strip() + "; \n")
f.close()

