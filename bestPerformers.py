#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:19:38 2021

@author: crystalhansen
"""

import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta




dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")


def logInfo( action,link, messg ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "stocks/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 
def makeSubCategoryDir(url, path):
    try:
        os.mkdir(path)
    except OSError:
        logInfo ("createDir", url,"Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    return


urlStock="https://fknol.com/ca/best-performing/basic-materials-stocks.php"

response= requests.get(urlStock)
stockSoup = BeautifulSoup(response.text,'lxml')

#
#fileName = "stocks/best_perform/basic-materials"+ d +".txt"
#f=open(fileName,"w")
#for article in stockSoup.find_all("article" , class_="w3-twothird w3-container"):
#    for article2 in article.find_all('article', class_="w3-half w3-container"):
#        for b in article2.find_all('b'):
#            print(b.text.strip() +",")
#            f.write(";" + b.text.strip() +",")
#            for href in b.find_all('a'):
#                print(href['href'] +",")
#                f.write(href['href'] +",")
#                #follow the link for individual stock information
#                name = href['href'].split("/")
#                
#                lenth = len(name)
#                
#                print(name[lenth-1])
#                symbol = name[lenth-1].split(".php")
#                print(symbol)
#                stockFile = "stocks/best_perform/"+ symbol[0]+ "_" + d +".txt"
#                response2 = requests.get(href['href'])
#                stockElSoup = BeautifulSoup(response2.text, 'lxml')
#                f3=open(stockFile,"w")
#                f3.write(symbol[0])
#                for product in stockElSoup.find_all('article' , class_='w3-twothird w3-container'):
#                    #print(product.text.strip())
#                    for table in product.find_all('table', class_="w3-table-twothird w3-striped w3-bordered w3-grey"):
#                        print("table")
#                        for tr in table.find_all("tr"):
#                            print(";")
#                            f3.write(";")
#                            for td in tr.find_all('td'):
#                                print(td)
#                                f3.write(td.text.strip() +" ,")
#                f3.close()
#                  
#        
#
#f.close() 
#       
#        
#fileName = "stocks/best_perform/links"+ d +".txt"
#f2=open(fileName,"w")
##all links
for article in stockSoup.find_all('article', class_="w3-third w3-container" ):
    for p in article.find_all('p', class_="w3-container"):
        print (p.text.strip())
        #f2.write(p.text.strip() +"\n\n")
        #f2.write("Category: " + p.text.strip() + "\n\n")
        for href in p.find_all('a'):
           # f2.write( href['href'] + "\n")
            print(href['href'])
            #f2.write("link: " + href.text.strip() )
            print(href.text.strip())
            name = href['href'].split("/")
            
            lenth = len(name)
            print(name[lenth-1])
            symbol = name[lenth-1].split(".php")
            print(symbol)
            path = "stocks/best_perform/"+symbol[0]
            makeSubCategoryDir(href['href'],path)
            
            stockFile = "stocks/best_perform/"+ symbol[0]+"/"+ symbol[0] +"_" + d +".txt"
            response2 = requests.get(href['href'])
            stockElSoup = BeautifulSoup(response2.text, 'lxml')
            f3=open(stockFile,"w")
            f3.write(symbol[0]+ "\n")
            f3.write(href['href'] + "\n")
            f3.write(href.text.strip() + "\n")
            for product in stockElSoup.find_all('article' , class_='w3-half w3-container'):
                #print(product.text.strip())
                #f3.write(product.text.strip())
                for b in product.find_all('b'):
                    print(b.text.strip())
                    f3.write(b.text.strip()+ "\n")
                    for href2 in b.find_all('a'):
                        print(href2['href'])
                        link = href2['href']
                        f3.write( link + ":" + href2.text.strip() + "\n")
                        ## need to follow this element href then wont need items below it. 
                        response3 = requests.get(link)
                        stockElSoup = BeautifulSoup(response3.text, 'lxml')
                        for artProduct in stockElSoup.find_all('article' , class_='w3-twothird w3-container'):
                            print(artProduct.text.strip())
                            for table in artProduct.find_all('table', class_="w3-table-twothird w3-striped w3-bordered w3-grey"):
#                                print("table")
#                                for tr in table.find_all("tr"):
#                                    print(";")
#                                    f3.write(";")
#                                    for td in tr.find_all('td'):
#                                        print(td)
#                                        f3.write(td.text.strip() +" ,")
                                        
                for ul in product.find_all("ul"):
                        print(";")
                        f3.write("; \n\n" + ul.text.strip())
                        for li in ul.find_all('li'):
                            print(li)
                            f3.write(li.text.strip() +" , \n\n")
        f3.close()
#    
#f2.close()    
#       
        
## get same data from https://finance.yahoo.com/quote/TMAS.CN?p=TMAS.CN then run comparisons against them
#use ticker from above and get data from yahoo

# include healthcare : motley fool top stocks undervalued including CWB ?? haha 
#TSX:VMD
#https://www.fool.ca/company/tsx-vmd-viemed-healthcare-inc/274006/
        
#TSX:GUD
#https://www.fool.ca/company/tsx-gud-knight-therapeutics-inc/273119/  
#TSX:AUP
#https://www.fool.ca/company/tsx-aup-aurinia-pharmaceuticals-inc/274733/
#TSX:ZYME
#https://www.fool.ca/company/tsx-zyme-zymeworks-inc/273780/ #nothing in it    
        
#scrape this page
#https://canada.swingtradebot.com/stocks-tagged-as/306-pharmaceutical

#yahoo cargojet
#https://ca.finance.yahoo.com/quote/CJT.TO/history?period1=1329091200&period2=1609545600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
#sovereign emerging market
#https://ca.finance.yahoo.com/quote/PCY/history?p=PCY&.tsrc=fin-srch
#MDNA
#https://www.cantechletter.com/stock-quotes/?qm_symbol=MDNA%3ACA
#https://investingnews.com/stock-information/?symbol=mdna:CA        
##1 Amgen (NASDAQ: AMGN)
#investing news
#https://investingnews.com/stock-information/?symbol=aps:CA
#https://investingnews.com/stock-information/?symbol=edt:CA     
#https://investingnews.com/stock-information/?symbol=szls:CA
#https://investingnews.com/stock-information/?symbol=hbp:CA
#Colonial Coal International (TSXV:CAD)
#https://investingnews.com/stock-information/?symbol=cad:ca
#Mangazeya Mining (TSXV:MGZ.H)
#https://investingnews.com/stock-information/?symbol=mgz.h:ca
#West High Yield Resources (TSXV:WHY)#https://investingnews.com/stock-information/?symbol=why:ca
#VanadiumCorp Resource (TSXV:VRB)
#https://investingnews.com/stock-information/?symbol=vrb:ca
#First Vanadium (TSXV:FVAN)
#https://investingnews.com/stock-information/?symbol=fvan:ca
#https://investingnews.com/stock-information/?symbol=mnd:ca
#https://investingnews.com/stock-information/?symbol=lgo:ca
#https://investingnews.com/stock-information/?symbol=meg:ca
#https://investingnews.com/stock-information/?symbol=vle:ca        