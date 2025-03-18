#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:16:12 2020

@author: crystalhansen
"""

from lxml import html

import urllib.request
import re 
from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

#grid-unit col-4-old content
#
#happifyResearchHTML = urllib.request.urlopen('https://www.happify.com/research/')
#happifySoup = bs.BeautifulSoup(happifyResearchHTML,'lxml')
#
##grid-row skill
#
#
#fileN= "research/happify_Research" + d +".txt"
#f=open(fileN,"w")
#f.write(happifySoup.title.string +"\n ")
#for li in happifySoup.find_all('div', class_='grid-row skill'):
#    print(li.text.strip()+", ")
#    f.write(li.text.strip()+";  \n")
#f.close()
#

  
def replaceABwithC(input, pattern, replaceWith): 
    return input.replace(pattern, replaceWith) 

 



scienceBlogLinks = urllib.request.urlopen('https://www.happify.com/public/science-of-happiness/')
blogSoupLinks = bs.BeautifulSoup(scienceBlogLinks,'lxml')

        
#        
#fileN= "research/happify_BlogTitles" + d +".txt"
#f=open(fileN,"w")
#f.write(blogSoupLinks.title.string +"\n ")

#res = [sub.replace('4', '1') for sub in test_list] 
for link in blogSoupLinks.find_all('a', class_= 'read-more',href=True):
     #print( link['href'] )
     

     link2 = link['href']
     preURL = link2[0:17]
     preURL2 = link2[0:4] 
     replaceWith = ''
    

     # substring  # s = s[ beginning : beginning + LENGTH]
     
     if(link2[0:17] == '/public/articles/'):
         # get link to /hd/file url to crawl and save
         #print("1."+  preURL)
         repLink = link2.replace(preURL, replaceWith)
         #strippedLink = link2[17:]
         #result = strippedLink.rstrip('\/')
         #print ("2."+  result ) 
         #repLink = link2.replace(preURL, replaceWith)
        # print( "3.a "+ repLink.rstrip('\/') )
         websiteUrl = 'https://www.happify.com/hd/'
         baseURL = 'https://www.happify.com/hd/' + repLink
        # print(baseURL)
         scienceBlogURL = urllib.request.urlopen(baseURL)
         articleSoup = bs.BeautifulSoup(scienceBlogURL,'lxml')
                 
         fileN= "research/public/articles/"+ repLink.rstrip('\/') + d +".txt"
         f=open(fileN,"w")
         f.write(articleSoup.title.string +"\n ")
        
         #print(articleSoup)
         for article in articleSoup.find_all('article', class_= 'article'):
            #print(article.text.strip())
            f.write(article.text.strip() +"\n ")
          
         
         f.close()

        
     elif(link2[0:4] == '/hd/'):
         #print("1.b "+  preURL2)
         repLink2 = link2.replace(preURL2, replaceWith)
         #result = repLink2.rstrip('\/')
         #print( "3.b "+ repLink2 )
         # get link to /hd/file url to crawl and save
         websiteUrl = 'https://www.happify.com/hd/'
         baseURL = 'https://www.happify.com/hd/' + repLink2
         #print(baseURL)
         scienceBlogURL = urllib.request.urlopen(baseURL)
         articleSoup = bs.BeautifulSoup(scienceBlogURL,'lxml')
                 
         fileN= "research/public/articles/"+ repLink2.rstrip('\/') + d +".txt"
         f=open(fileN,"w")
         f.write(articleSoup.title.string +"\n ")
        
         #print(articleSoup)
         for article in articleSoup.find_all('article', class_= 'article'):
           # print(article.text.strip())
            f.write(article.text.strip() +"\n ")

         f.close()
     else:
        print('other')
         # skip
         
    #if(pattern exists in then)    
    #pattern = '\/public/articles\/'
    #replaceWith = ' '
    #print (replaceABwithC(link2,pattern,replaceWith) )
#else pattern="/hd/"  replaceWith = ' '

#     f.write ( result + "  \n" )
#
#f.close()
