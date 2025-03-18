#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:02:29 2020

@author: crystalhansen
"""

from lxml import html
import requests
import re 
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

 
dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

anniesRemedies = "https://www.anniesremedy.com/chart.php?alpha="
alpha=['a','b','c','d','e','f','g','H','I', 'J', 'K', 'L', 'M', 'N', 'O' ,'P', 'Q', 'R','S' ,'T', 'U', 'V', 'W', 'X', 'Y' ,'Z']
#embeddedLinks =[]
for alph in alpha:
    print(alph)
    #alph = "a" ##testing purposes
    remedyURL = anniesRemedies + alph
    print(remedyURL)
    response = requests.get(remedyURL)
    soup = BeautifulSoup(response.text)
    #print (soup)
    websiteBaseUrl = "https://www.anniesremedy.com/"
    
        
    for link in soup.find_all('a', class_= 'sitelist',href=True):
        link2 = link['href']
        #print(link.text.strip() + " ::: " + link2)
         #preURL = link2[0:17]
         #preURL2 = link2[0:4] 
         #replaceWith = ''
        #print(link2 + "; \n")
       
        baseURL = websiteBaseUrl + link2
        print(baseURL)
        response = requests.get(baseURL)
        herbSoup = BeautifulSoup(response.text,'lxml')
        
        title=herbSoup.title.string
        
        fileN= "anniesRemedies/herbsA-Z/AnniesRemedies_" + title +".txt"
        
       
        f=open(fileN,"w")
        f.write(soup.title.string +"\n" + baseURL + "\n")
        print(soup.title.string +"\n"+ baseURL + "\n")
        #print(herbSoup)             
        for article in herbSoup.find_all('div', class_= 'herbbox'):
            #print(herbSoup.title.string +"\n")
            f.write(herbSoup.title.string +"||| \n")
            #print(article.text.strip())
            f.write(article.text.strip() +"\n\n\n ")
        for articleLink in herbSoup.find_all('a', class_='tag', href=True):
            artLink = articleLink['href']
            print(artLink + "; \n")
            f2.write(artLink +"; \n ")
            #embeddedLinks.append(artLink)
        f.close()
        

print("Im Done!!!")