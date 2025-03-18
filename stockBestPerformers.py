#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:36:34 2021

@author: crystalhansen
"""


import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta

#etsy.com, ebay.com, eled.com


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")


def logInfo( action,link, messg ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "scrapers/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 



#https://fknol.com/ca/best-performing/
# 'p', class_='w3-container'