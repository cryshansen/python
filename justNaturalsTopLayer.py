#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:46:55 2021

@author: crystalhansen
"""


from lxml import html
import requests

from bs4 import BeautifulSoup
from datetime import datetime, timedelta

map=[]
url = 'http://www.justnaturalskincare.com/hair-gray/all-gray-hair.html'

response= requests.get(url)
jNSoup= BeautifulSoup(response.text,'lxml')
print (jNSoup.title.string)


# NOT WORKING FILE
for div in jNSoup.find_all('div', id="e8"):
    #print(div)
    
for table_row_cell in jNSoup.select("table tr td "):
   # print("table row")
    for table_row_cell2 in table_row_cell.select('table tr td'):
        #print("tablerow2")
        for table_row_cell3 in table_row_cell2.select('table tr td'):
            #print("table3")
            for table_row_cell4 in table_row_cell3.select('table tr td'):
                #print("table4")
                for table5 in table_row_cell.select('table'):
                    #print(table5)
                    count=0
                    for row in table5.select('tr td'):
                        count+=1
                        #print(row.text.strip())
                        if(count == 5):
                            
                            for href in row.select('a'):
                               link = href['href']
                               category = href['href'].split("/")
                               #print(category)
                               if(len(category) == 1):
                                ### bind to a hashtable and compare if alread in table then omit fro calling request
                                # python check if key in dict using "in"
                                if link in map:
                                    print(f"Yes, key: '{link}' exists in dictionary")
                                else:
                                    print(f"No, key: '{link}' does not exists in dictionary")
                                    map.append(href['href'])
                                #print(href['href'])
#                                url2 = 'http://www.justnaturalskincare.com'
#                                builtUrl = url2 + "/" +href['href']
#                                print(builtUrl)
                            
                        
            
#    for tables in div.find_all('table'):
#        
#        for tablebody in tables.find_all('tbody'):
#            for tr in tablebody.find_all('tr'):
#                for td in tr.find_all('td'):
#                    print(td)
#    for anode in div.find_all('a'):
#        print(anode['href'])
        #category = anode['href'].split("/")