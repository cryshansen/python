#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:37:18 2021

@author: crystalhansen

this file scrapes the just naturals site for its soap and cream contents 


working file, needs to parse the textual content better and transverse over the links in a better way
"""
from lxml import html
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
map=[]
dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S") 
## get urls for jNaturals and eliminate repeats then loop through the map of site to get individual elements

urlBase = "http://www.justnaturalskincare.com/"

url = 'http://www.justnaturalskincare.com/9/antiaging/-ANTI-AGING.html'
ext = 'html'

def logInfo( action,link, messg ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "justNaturals/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 




def listFD(url, ext):
    page = requests.get(url).text
    #print (page)
    soup = BeautifulSoup(page, 'html.parser')
    return [ node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

fileBase = "justNaturals/"
fileBaseCat = "antiaging/"


#capture the links to a file to use if all else fails
filename="justNaturals/hrefs.txt"

f=open(filename,"w")
for href in listFD(url, ext):
    #print (href)
    f.write(href +"\n\n")
    ## split the href because grabs all hrefs on page we want to transverse these links and grab all page content of individual produtcs
    category = href.split("/")
    ## if same level content links means either in section we have our link aka anti-aging 
    if(len(category) == 1):
        urlBase1 = 'http://www.justnaturalskincare.com/9/antiaging/'
        link = urlBase1 + href
        
        response= requests.get(link)
        jNSoup= BeautifulSoup(response.text,'lxml')
        if(jNSoup.title is None):
            print("none")
            logInfo("getUrl", link, "title is None")
        else: 
            filename =fileBase + fileBaseCat +  jNSoup.title.string + ".txt"
            
            f2 = open(filename,"w")
            f2.write(jNSoup.title.string +"\n\n")
            print(jNSoup.title.string  +"\n\n")
            f2.write(jNSoup.text.strip() +"\n\n")
            print(jNSoup.text.strip() +"\n\n")
#            for anode in jNSoup.find_all('a'):
#                link2 = anode['href']
#                f.write(link2 + "\n\n")
            f2.close()
    elif(len(category) ==3 ):
        
        linkPath =""
        #check if top level or other subcategory
        if(category[1] != ".."):
            #used for creating directory file writing
            fileBaseCat = category[1]
            print(urlBase + category[1] +"/"+category[2] +"\n\n")
            #write what link we made to debug if required turn into logInfo()
            f.write(urlBase + category[1] +"/"+category[2] +"\n\n")
            linkPath = urlBase + category[1] +"/"+category[2]
        else:
            #ignore category[1] because is ".." threfore top level
            print(urlBase +category[2] +"\n\n")
            #write what link we made to debug if required turn into logInfo()
            f.write(urlBase +category[2] +"\n\n")
            linkPath = urlBase +category[2]
            
        #once link is built call request and handle data.    
        if(linkPath != ""):
            response1= requests.get(linkPath)
            jNSoup= BeautifulSoup(response1.text,'lxml')
            if(jNSoup.title is None):
                print("none")
                logInfo("getUrl", linkPath, "title is None")
            else: 
                filename =fileBase + fileBaseCat +"/" +  jNSoup.title.string + ".txt"
                
                f3 = open(filename,"w")
                f3.write(jNSoup.title.string +"\n\n")
                print(jNSoup.title.string  +"\n\n")
                f3.write(jNSoup.text.strip() +"\n\n")
                print(jNSoup.text.strip() +"\n\n")
                f3.close()
f.close()