#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:03:18 2020

@author: crystalhansen
"""


import urllib.request
import re 
from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

#https://www.frontiersin.org/articles/10.3389/fpsyt.2016.00215/full

#scienceBlogLinks = urllib.request.urlopen('https://www.frontiersin.org/articles/10.3389/fpsyt.2016.00215/full')
#articleSoup = bs.BeautifulSoup(scienceBlogLinks,'lxml')
#
#title = articleSoup.title.string
##link2[0:17]
#pageTitle = title[0:45] 
#
#
#fileN= "research_articles/Frontiersin"+ pageTitle +  d +".txt"
#f=open(fileN,"w")
#f.write(articleSoup.title.string +"\n ")
#
#for article in articleSoup.find_all('div', class_= 'abstract-container'):
###     #print( link['href'] )
#     print(article.text.strip() + "\n")
#     f.write(article.text.strip() +"\n ")
#f.close()




liebertLinks = urllib.request.urlopen('https://www.liebertpub.com/doi/full/10.1089/g4h.2017.0150')
articleSSoup = bs.BeautifulSoup(liebertLinks,'lxml')

print(articleSSoup.title.string)

#
for article in articleSSoup.find_all('div', class_= 'article__content'):
     print(article.text.strip() + "\n")
     #f.write(article.text.strip() +"\n ")