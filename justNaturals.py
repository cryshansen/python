#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:56:13 2020

@author: crystalhansen

Non working file saved for python snippets



"""

from lxml import html
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S") 
soup = ""

def logInfo( action,link, messg ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "justNaturals/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 

def makeSubCategoryDir(url, path):
    basePath = "justNaturals/"
    fullPath = basePath + path
    try:
       if not os.path.exists(fullPath):
        os.mkdir(fullPath)
    except OSError:
        logInfo ("createDir", url,"Creation of the directory %s failed" % fullPath)
    else:
        print ("Successfully created the directory %s " % fullPath)
    
    return


def getTable():
    #find tables    

    table = soup.find('table', id="data")
    for row in table.find_all("tr")[1:]:  # skipping header row
        cells = row.find_all("td")
        print(cells[0].text, cells[1].find('a').text)
    
    return

    

def getAllTables(jNsoup):
    
#jNSoup.prettify()

    tables = jNSoup.find_all("tbody")
    
    storeTable = tables[0].find_all("tr")
    storeValueRows = tables[2].find_all("tr")
    
    storeRank = []
    for row in storeTable:
        storeRank.append(row.get_text().strip())
    
    storeMatrix = []
    for row in storeValueRows:
        storeMatrixRow = []
        for cell in row.find_all("td")[::2]:
            storeMatrixRow.append(cell.get_text().strip())
        storeMatrix.append(", ".join(storeMatrixRow))
    
    for record in zip(storeRank, storeMatrix):
        print (" ".join(record)  )  
    
    return





urlBase = "http://www.justnaturalskincare.com/"

url = 'http://www.justnaturalskincare.com'
ext = 'html'

def listFD(url, ext):
    page = requests.get(url).text
    #print (page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for file in listFD(url, ext):
     print (file) 
     response= requests.get(file)
     jNSoup= BeautifulSoup(response.text,'lxml')
     print (jNSoup.title.string)
     for anode in jNSoup.find_all('a'):
         #print(anode['href'] )
         #means has a different subcategory
         #link = anode['href'].find("../")
         category = anode['href'].split("/")
         #print(category)
         if(len(category) == 3):
             print(category[1] + category[2])
             #makeSubCategoryDir(urlBase,category[1])
             newU = urlBase + category[1]+ "/"+ category[2]
             print("~~~~~~~~~~~~~~ category[3]")
             print(newU)
             
             try:
                 subCats = requests.get(newU)
                 jSubCats = BeautifulSoup( subCats.text, 'lxml')
             
             except HTTPError as e:
                 
                 print("No Data")
                 
             else:    
                 print(jSubCats.title.string)
                 title = jSubCats.title.string #if div.find("li", "item-engine") else ''
                 fileloc = "justNaturals/"+category[1] +"/" + title +".txt"
                 div = jSubCats.find_all('div', id="e2")
                 f=open(fileloc,"w")
                 f.write(title + "\n")
                 
                 
                 #tables = div.find_all('tbody')
                 for table in div:
                     f.write(table.get_text().strip() +"\n")
                 
    #                storeTable = table.find_all("tr")
    #                for row in storeTable:
    #                    #print(row)
    #                    for cell in row.find_all("td"):
    #                        print(cell.get_text().strip() + "\n")
                 
                 
                 for subcatNode in jSubCats.find_all('a', href=True):
                     print(subcatNode['href'])
                     f.write(subcatNode['href']+"\n")
    #                 newUr = urlBase + node
    #                 print(newUr)
    #                 subCats = requests.get(newUr)
    #                 jSubCats2 = BeautifulSoup( subCats2.text, 'lxml')
    #                 print(jSubCats2.title.string)
    #                 tables = jSubCats.find_all('tbody')
    #                 for table in tables:
    #                    storeTable = table.find_all("tr")
    #                    for row in storeTable:
    #                        #print(row)
    #                        for cell in row.find_all("td"):
    #                            print(cell.get_text().strip() + "\n")
                 f.close()
             
         elif(len(category) == 1):
            print(category[0])
         #means its top level content 
         #elif(link == -1):
             
            #print(anode['href'])
            newU = urlBase + anode['href']
            print("~~~~~~~~~~~~~~ single page")
            print(newU)
            try:
                subCats = requests.get(newU)
                jSubCats = BeautifulSoup( subCats.text, 'lxml')
                print(jSubCats)
            except HTTPError as e:
                 print("No Data" + e)
            else:
                
                if(jSubCats.title is None):
                    print("error")    
                else:
                    jTitle = jSubCats.title.string
                    print(jTitle)
                    fileName = "justNaturals/"+ jTitle + ".txt"
                    f=open(fileName,"w")
                    
                    tables = jSubCats.find_all('tbody')
                    for table in tables:
                        f.write(table)
                        storeTable = table.find_all("tr")
                        for row in storeTable:
                            f.write(row + "\n")
                            for cell in row.find_all("td"):
                                f.write(cell.get_text().strip() + "\n")
                        
            #read the file
         #substring() # pr trim first three chars
         
         
    
    