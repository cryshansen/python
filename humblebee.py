#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:57:50 2020

@author: crystalhansen
"""



from lxml import html
import requests

from bs4 import BeautifulSoup
from datetime import datetime, timedelta

dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

def logInfo( action,link ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "humblebee/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 


#step 1 build url
#step 2 open request
#setp 3 get response
#step 4 do something iterate response for content and links
    # for each response  get links get content  
    #    for each link capture content and links
    #write to files

basicURL = "https://www.humblebeeandme.com/recipe-index/"

response = requests.get(basicURL)
soup = BeautifulSoup(response.text,'lxml')
#print (soup)
#websiteBaseUrl = "https://www.humblebeeandme.com/"
for link in soup.find_all('article'):
    #print(link) 
    for href in link.find_all('a',href=True):
        link = href['href']
        logInfo("href: ", link)
        #print(link)
        articleResponse = requests.get(link)
        articleSoup = BeautifulSoup(articleResponse.text,'lxml')
        soupTitle = articleSoup.title.string
        print(soupTitle)
        logInfo("title", soupTitle)
        soupTitle = soupTitle.replace("/", "_")
        fileN= "humblebee/articles/" + soupTitle +"_"+d+".txt"
        
        f=open(fileN,"w")
        f.write(soupTitle +"\n" + link + "\n")
        
        
        for article in articleSoup.find_all('div', class_="entry-content"):
             #print(article.text.strip())
             f.write(article.text.strip())
             
        f.close()
            