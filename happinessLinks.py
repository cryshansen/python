#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:04:40 2020

@author: crystalhansen
"""
websiteUrl = 'https://www.happify.com/hd/'
#websub = '/public/articles/'
linkHTML = 'what-is-happiness-anyway'
buildString = websiteUrl+linkHTML +'/'
print(buildString)
scienceBlogLinks = urllib.request.urlopen(buildString)

articleSoup = bs.BeautifulSoup(scienceBlogLinks,'lxml')

        
        
fileN= "research/public/articles/"+ linkHTML + d +".txt"
f=open(fileN,"w")
#f.write(articleSoup.title.string +"\n ")

#print(articleSoup)
for article in articleSoup.find_all('article', class_= 'article'):

   print(article.text.strip())
  #f.write(article.text.strip() +"\n ")
  
 
f.close()
